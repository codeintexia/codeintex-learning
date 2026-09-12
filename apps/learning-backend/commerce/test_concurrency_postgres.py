import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from threading import Barrier
from unittest import skipUnless

from django.contrib.auth import get_user_model
from django.db import IntegrityError, close_old_connections, connection, transaction
from django.test import TransactionTestCase
from django.utils import timezone

from learning.models import Course, CourseRelease, Enrollment

from .models import CourseOffer, Order, Payment
from .models import CourseEntitlement

from .models import ProviderEvent

from .services import (
    OpenOrderExistsError,
    PayablePaymentExistsError,
    create_order,
    create_payment,
    fulfill_purchase,
    process_provider_event,
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

@skipUnless(
    connection.vendor == "postgresql",
    "PostgreSQL concurrency test",
)
class PurchaseFulfillmentConcurrencyTests(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="fulfillment-concurrency-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="fulfillment-concurrency-course",
            subject="Backend Engineering",
            title="Fulfillment Concurrency Course",
            summary="Concurrent purchase fulfillment acceptance test.",
        )
        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Fulfillment Concurrency Course R1",
            summary="Published release for fulfillment concurrency.",
            is_published=True,
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
        self.payment = create_payment(
            order=self.order,
            provider="test-provider",
        )
        self.payment.status = Payment.Status.SUCCEEDED
        self.payment.succeeded_at = timezone.now()
        self.payment.save(
            update_fields=[
                "status",
                "succeeded_at",
            ]
        )

    def _fulfill_purchase(self, barrier):
        close_old_connections()

        try:
            payment = Payment.objects.get(pk=self.payment.pk)

            barrier.wait(timeout=10)

            fulfill_purchase(payment=payment)
            return "fulfilled"
        finally:
            close_old_connections()

    def test_concurrent_fulfillment_is_idempotent(self):
        barrier = Barrier(2)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(
                    self._fulfill_purchase,
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
            ["fulfilled", "fulfilled"],
        )

        self.assertEqual(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).count(),
            1,
        )

        self.assertEqual(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).count(),
            1,
        )

        self.order.refresh_from_db()

        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )
        self.assertIsNotNone(self.order.fulfilled_at)

@skipUnless(
    connection.vendor == "postgresql",
    "PostgreSQL concurrency test",
)
class ProviderEventProcessingConcurrencyTests(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="provider-event-concurrency-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="provider-event-concurrency-course",
            subject="Backend Engineering",
            title="Provider Event Concurrency Course",
            summary="Concurrent ProviderEvent processing acceptance test.",
        )
        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Provider Event Concurrency Course R1",
            summary="Published release for event concurrency testing.",
            is_published=True,
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
        self.payment = create_payment(
            order=self.order,
            provider="test-provider",
        )
        self.event = ProviderEvent.objects.create(
            provider="test-provider",
            payment=self.payment,
            merchant_reference=self.payment.merchant_reference,
            provider_event_id="concurrent-event-1",
            provider_transaction_id="concurrent-tx-1",
            event_type="payment-status",
            provider_status="raw-success",
            amount_minor=self.payment.amount_minor,
            currency=self.payment.currency,
            payload_digest="concurrent-event-digest",
            authenticity_verified_at=timezone.now(),
            authenticity_method="test-signature",
        )

    def _process_event(self, barrier):
        close_old_connections()

        try:
            event = ProviderEvent.objects.get(pk=self.event.pk)

            barrier.wait(timeout=10)

            process_provider_event(
                provider_event=event,
                observed_payment_status=Payment.Status.SUCCEEDED,
            )
            return "processed"
        finally:
            close_old_connections()

    def test_concurrent_processing_has_one_effective_processor(self):
        barrier = Barrier(2)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [
                executor.submit(
                    self._process_event,
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
            ["processed", "processed"],
        )

        self.event.refresh_from_db()
        self.payment.refresh_from_db()
        self.order.refresh_from_db()

        self.assertEqual(
            self.event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )
        self.assertEqual(
            self.event.attempt_count,
            1,
        )

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )

        self.assertEqual(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).count(),
            1,
        )

        self.assertEqual(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).count(),
            1,
        )
