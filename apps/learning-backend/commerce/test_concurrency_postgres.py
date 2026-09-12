import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from threading import Barrier
from unittest import skipUnless

from django.contrib.auth import get_user_model
from django.db import IntegrityError, close_old_connections, connection, transaction
from django.test import TransactionTestCase
from django.utils import timezone

from learning.models import Course

from .models import CourseOffer, Order, Payment
from .services import (
    OpenOrderExistsError,
    PayablePaymentExistsError,
    create_order,
    create_payment,
)


@skipUnless(
    connection.vendor == "postgresql",
    "PostgreSQL concurrency test",
)
class OrderConcurrencyTests(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="concurrency-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="concurrency-course",
            subject="Backend Engineering",
            title="Concurrency Course",
            summary="Concurrency acceptance test course.",
        )
        self.offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=500_000,
            currency="IDR",
            is_active=True,
        )

    def _create_open_order(self, barrier):
        close_old_connections()

        try:
            barrier.wait(timeout=10)

            try:
                with transaction.atomic():
                    Order.objects.create(
                        learner_id=self.learner.pk,
                        course_id=self.course.pk,
                        offer_id=self.offer.pk,
                        status=Order.Status.OPEN,
                        subtotal_amount_minor=500_000,
                        discount_amount_minor=0,
                        total_amount_minor=500_000,
                        currency="IDR",
                        course_title_snapshot=self.course.title,
                        expires_at=timezone.now()
                        + timedelta(minutes=30),
                    )
                return "created"
            except IntegrityError:
                return "integrity_error"
        finally:
            close_old_connections()

    def test_two_concurrent_creates_allow_only_one_open_order(self):
        barrier = Barrier(2)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(self._create_open_order, barrier)
                for _ in range(2)
            ]
            results = [future.result(timeout=15) for future in futures]

        self.assertCountEqual(
            results,
            ["created", "integrity_error"],
        )
        self.assertEqual(
            Order.objects.filter(
                learner=self.learner,
                course=self.course,
                status=Order.Status.OPEN,
            ).count(),
            1,
        )

@skipUnless(
    connection.vendor == "postgresql",
    "PostgreSQL concurrency test",
)
class PaymentConcurrencyTests(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="payment-concurrency-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="payment-concurrency-course",
            subject="Backend Engineering",
            title="Payment Concurrency Course",
            summary="Payment concurrency acceptance test course.",
        )
        self.offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=500_000,
            currency="IDR",
            is_active=True,
        )
        self.order = Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=self.offer,
            status=Order.Status.OPEN,
            subtotal_amount_minor=500_000,
            discount_amount_minor=0,
            total_amount_minor=500_000,
            currency="IDR",
            course_title_snapshot=self.course.title,
            expires_at=timezone.now() + timedelta(minutes=30),
        )

    def _create_payable_payment(self, barrier):
        close_old_connections()

        try:
            barrier.wait(timeout=10)

            try:
                with transaction.atomic():
                    Payment.objects.create(
                        order_id=self.order.pk,
                        provider="test-provider",
                        status=Payment.Status.CREATED,
                        operation_key=uuid.uuid4(),
                        merchant_reference=f"payment-{uuid.uuid4()}",
                        amount_minor=500_000,
                        currency="IDR",
                    )
                return "created"
            except IntegrityError:
                return "integrity_error"
        finally:
            close_old_connections()

    def test_two_concurrent_checkout_creates_allow_only_one_payable_payment(
        self,
    ):
        barrier = Barrier(2)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(
                    self._create_payable_payment,
                    barrier,
                )
                for _ in range(2)
            ]
            results = [
                future.result(timeout=15)
                for future in futures
            ]

        self.assertCountEqual(
            results,
            ["created", "integrity_error"],
        )
        self.assertEqual(
            Payment.objects.filter(
                order=self.order,
                status__in=[
                    Payment.Status.CREATED,
                    Payment.Status.PENDING,
                ],
            ).count(),
            1,
        )

@skipUnless(
    connection.vendor == "postgresql",
    "PostgreSQL concurrency test",
)
class CreateOrderServiceConcurrencyTests(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="service-concurrency-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="service-concurrency-course",
            subject="Backend Engineering",
            title="Service Concurrency Course",
            summary="Service-level concurrency acceptance test.",
        )
        self.offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=500_000,
            currency="IDR",
            is_active=True,
        )

    def _create_order(self, barrier):
        close_old_connections()

        try:
            learner = get_user_model().objects.get(
                pk=self.learner.pk,
            )
            course = Course.objects.get(pk=self.course.pk)

            barrier.wait(timeout=10)

            try:
                create_order(
                    learner=learner,
                    course=course,
                    offer_id=self.offer.pk,
                    expires_at=(
                        timezone.now()
                        + timedelta(minutes=30)
                    ),
                )
                return "created"
            except OpenOrderExistsError:
                return "open_order_exists"
        finally:
            close_old_connections()

    def test_concurrent_create_order_serializes_per_learner_course(
        self,
    ):
        barrier = Barrier(2)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(self._create_order, barrier)
                for _ in range(2)
            ]
            results = [
                future.result(timeout=15)
                for future in futures
            ]

        self.assertCountEqual(
            results,
            ["created", "open_order_exists"],
        )

        self.assertEqual(
            Order.objects.filter(
                learner=self.learner,
                course=self.course,
                status=Order.Status.OPEN,
            ).count(),
            1,
        )

@skipUnless(
    connection.vendor == "postgresql",
    "PostgreSQL concurrency test",
)
class CreatePaymentServiceConcurrencyTests(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="payment-service-concurrency-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="payment-service-concurrency-course",
            subject="Backend Engineering",
            title="Payment Service Concurrency Course",
            summary="Payment service concurrency acceptance test.",
        )
        self.offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=500_000,
            currency="IDR",
            is_active=True,
        )
        self.order = create_order(
            learner=self.learner,
            course=self.course,
            offer_id=self.offer.pk,
            expires_at=timezone.now() + timedelta(minutes=30),
        )

    def _create_payment(self, barrier):
        close_old_connections()

        try:
            order = Order.objects.get(pk=self.order.pk)

            barrier.wait(timeout=10)

            try:
                create_payment(
                    order=order,
                    provider="test-provider",
                )
                return "created"
            except PayablePaymentExistsError:
                return "payable_payment_exists"
        finally:
            close_old_connections()

    def test_concurrent_create_payment_serializes_per_order(self):
        barrier = Barrier(2)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(self._create_payment, barrier)
                for _ in range(2)
            ]
            results = [
                future.result(timeout=15)
                for future in futures
            ]

        self.assertCountEqual(
            results,
            ["created", "payable_payment_exists"],
        )

        self.assertEqual(
            Payment.objects.filter(
                order=self.order,
                status__in=[
                    Payment.Status.CREATED,
                    Payment.Status.PENDING,
                ],
            ).count(),
            1,
        )
