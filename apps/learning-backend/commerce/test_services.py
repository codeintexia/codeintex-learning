import uuid
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from learning.models import Course

from .models import CourseEntitlement, CourseOffer, Order, Payment
from .services import (
    ActivePurchaseEntitlementError,
    OpenOrderExistsError,
    OrderNotPayableError,
    PayablePaymentExistsError,
    SuccessfulPaymentExistsError,
    create_order,
    create_payment,
)


class CreateOrderServiceTests(TestCase):
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="create-order-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="create-order-course",
            subject="Backend Engineering",
            title="Create Order Course",
            summary="Service contract test course.",
        )
        self.offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=500_000,
            currency="IDR",
            is_active=True,
        )

    def test_creates_server_authoritative_commercial_snapshot(self):
        expires_at = timezone.now() + timedelta(minutes=30)

        order = create_order(
            learner=self.learner,
            course=self.course,
            offer_id=self.offer.pk,
            expires_at=expires_at,
        )

        self.assertEqual(order.status, Order.Status.OPEN)
        self.assertEqual(order.offer, self.offer)
        self.assertEqual(order.subtotal_amount_minor, 500_000)
        self.assertEqual(order.discount_amount_minor, 0)
        self.assertEqual(order.total_amount_minor, 500_000)
        self.assertEqual(order.currency, "IDR")
        self.assertEqual(
            order.course_title_snapshot,
            self.course.title,
        )
        self.assertEqual(order.expires_at, expires_at)

    def test_expires_stale_open_order_before_creating_replacement(self):
        stale = Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=self.offer,
            status=Order.Status.OPEN,
            subtotal_amount_minor=500_000,
            discount_amount_minor=0,
            total_amount_minor=500_000,
            currency="IDR",
            course_title_snapshot=self.course.title,
            expires_at=timezone.now() - timedelta(minutes=1),
        )

        replacement = create_order(
            learner=self.learner,
            course=self.course,
            offer_id=self.offer.pk,
            expires_at=timezone.now() + timedelta(minutes=30),
        )

        stale.refresh_from_db()

        self.assertEqual(stale.status, Order.Status.EXPIRED)
        self.assertEqual(replacement.status, Order.Status.OPEN)
        self.assertNotEqual(replacement.pk, stale.pk)

    def test_rejects_when_live_open_order_exists(self):
        existing = Order.objects.create(
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

        with self.assertRaises(OpenOrderExistsError):
            create_order(
                learner=self.learner,
                course=self.course,
                offer_id=self.offer.pk,
                expires_at=timezone.now() + timedelta(minutes=30),
            )

        self.assertEqual(
            Order.objects.filter(
                learner=self.learner,
                course=self.course,
                status=Order.Status.OPEN,
            ).count(),
            1,
        )
        existing.refresh_from_db()
        self.assertEqual(existing.status, Order.Status.OPEN)

    def test_rejects_when_active_purchase_entitlement_exists(self):
        fulfilled_order = Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=self.offer,
            status=Order.Status.FULFILLED,
            subtotal_amount_minor=500_000,
            discount_amount_minor=0,
            total_amount_minor=500_000,
            currency="IDR",
            course_title_snapshot=self.course.title,
            expires_at=timezone.now() + timedelta(minutes=30),
            fulfilled_at=timezone.now(),
        )
        CourseEntitlement.objects.create(
            learner=self.learner,
            course=self.course,
            source=CourseEntitlement.Source.PURCHASE,
            status=CourseEntitlement.Status.ACTIVE,
            order=fulfilled_order,
            grant_reason="test purchase",
        )

        with self.assertRaises(ActivePurchaseEntitlementError):
            create_order(
                learner=self.learner,
                course=self.course,
                offer_id=self.offer.pk,
                expires_at=timezone.now() + timedelta(minutes=30),
            )

        self.assertFalse(
            Order.objects.filter(
                learner=self.learner,
                course=self.course,
                status=Order.Status.OPEN,
            ).exists()
        )

class CreatePaymentServiceTests(TestCase):
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="create-payment-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="create-payment-course",
            subject="Backend Engineering",
            title="Create Payment Course",
            summary="Payment service contract test course.",
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

    def test_creates_server_authoritative_payment(self):
        payment = create_payment(
            order=self.order,
            provider="test-provider",
        )

        self.assertEqual(payment.order, self.order)
        self.assertEqual(payment.provider, "test-provider")
        self.assertEqual(payment.status, Payment.Status.CREATED)
        self.assertEqual(payment.amount_minor, self.order.total_amount_minor)
        self.assertEqual(payment.currency, self.order.currency)
        self.assertIsNotNone(payment.operation_key)
        self.assertTrue(payment.merchant_reference)

    def test_rejects_closed_order(self):
        self.order.status = Order.Status.CANCELLED
        self.order.save(update_fields=["status"])

        with self.assertRaises(OrderNotPayableError):
            create_payment(
                order=self.order,
                provider="test-provider",
            )

    def test_rejects_existing_successful_payment(self):
        Payment.objects.create(
            order=self.order,
            provider="test-provider",
            status=Payment.Status.SUCCEEDED,
            operation_key=uuid.uuid4(),
            merchant_reference=f"payment-{uuid.uuid4()}",
            provider_transaction_id=f"tx-{uuid.uuid4()}",
            amount_minor=self.order.total_amount_minor,
            currency=self.order.currency,
            succeeded_at=timezone.now(),
        )

        with self.assertRaises(SuccessfulPaymentExistsError):
            create_payment(
                order=self.order,
                provider="test-provider",
            )

    def test_rejects_existing_payable_payment(self):
        Payment.objects.create(
            order=self.order,
            provider="test-provider",
            status=Payment.Status.PENDING,
            operation_key=uuid.uuid4(),
            merchant_reference=f"payment-{uuid.uuid4()}",
            amount_minor=self.order.total_amount_minor,
            currency=self.order.currency,
        )

        with self.assertRaises(PayablePaymentExistsError):
            create_payment(
                order=self.order,
                provider="test-provider",
            )
