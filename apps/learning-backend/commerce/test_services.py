import uuid
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.test import TestCase
from django.utils import timezone

from learning.models import Course, CourseRelease, Enrollment

from .models import (
    CourseEntitlement,
    CourseOffer,
    FinancialAdjustment,
    Order,
    Payment,
    PaymentIntegrityCase,
    ProviderEvent,
)
from .services import (
    ActivePurchaseEntitlementError,
    OpenOrderExistsError,
    OrderNotFulfillableError,
    OrderNotPayableError,
    PayablePaymentExistsError,
    PaymentNotSuccessfulError,
    PublishedCourseReleaseRequiredError,
    SuccessfulPaymentExistsError,
    AdjustmentCurrencyMismatchError,
    AdjustmentNotConfirmableError,
    ExcessiveFinancialAdjustmentError,
    apply_payment_observation,
    confirm_financial_adjustment,
    create_order,
    create_payment,
    fulfill_purchase,
    process_provider_event,
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

class PurchaseFulfillmentServiceTests(TestCase):
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="fulfillment-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="fulfillment-course",
            subject="Backend Engineering",
            title="Fulfillment Course",
            summary="Purchase fulfillment service test course.",
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

    def create_published_release(self, release_number):
        return CourseRelease.objects.create(
            course=self.course,
            release_number=release_number,
            title=f"Fulfillment Course R{release_number}",
            summary="Published release for fulfillment testing.",
            is_published=True,
        )

    def mark_payment_succeeded(self):
        self.payment.status = Payment.Status.SUCCEEDED
        self.payment.succeeded_at = timezone.now()
        self.payment.save(
            update_fields=[
                "status",
                "succeeded_at",
            ]
        )

    def test_successful_payment_fulfills_purchase_atomically(self):
        release = self.create_published_release(1)
        self.mark_payment_succeeded()

        fulfill_purchase(payment=self.payment)

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )
        enrollment = Enrollment.objects.get(
            learner=self.learner,
            course_release=release,
        )
        self.order.refresh_from_db()

        self.assertEqual(
            entitlement.source,
            CourseEntitlement.Source.PURCHASE,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )
        self.assertEqual(entitlement.learner, self.learner)
        self.assertEqual(entitlement.course, self.course)

        self.assertEqual(enrollment.course_release, release)

        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )
        self.assertIsNotNone(self.order.fulfilled_at)

    def test_retry_is_idempotent_and_preserves_original_release(self):
        release_1 = self.create_published_release(1)
        self.mark_payment_succeeded()

        fulfill_purchase(payment=self.payment)

        self.create_published_release(2)

        fulfill_purchase(payment=self.payment)

        self.assertEqual(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).count(),
            1,
        )
        self.assertEqual(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release__course=self.course,
            ).count(),
            1,
        )
        self.assertTrue(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=release_1,
            ).exists()
        )

    def test_rejects_payment_that_is_not_successful(self):
        self.create_published_release(1)

        with self.assertRaises(PaymentNotSuccessfulError):
            fulfill_purchase(payment=self.payment)

        self.assertFalse(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).exists()
        )

    def test_rejects_successful_payment_for_closed_order(self):
        self.create_published_release(1)

        self.order.status = Order.Status.EXPIRED
        self.order.save(update_fields=["status"])

        self.mark_payment_succeeded()

        with self.assertRaises(OrderNotFulfillableError):
            fulfill_purchase(payment=self.payment)

        self.assertFalse(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).exists()
        )

    def test_requires_current_published_course_release(self):
        self.mark_payment_succeeded()

        with self.assertRaises(
            PublishedCourseReleaseRequiredError
        ):
            fulfill_purchase(payment=self.payment)

        self.order.refresh_from_db()

        self.assertEqual(self.order.status, Order.Status.OPEN)
        self.assertFalse(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).exists()
        )
        self.assertFalse(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release__course=self.course,
            ).exists()
        )

class ProviderEventProcessingServiceTests(TestCase):
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="provider-event-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="provider-event-course",
            subject="Backend Engineering",
            title="Provider Event Course",
            summary="ProviderEvent processing service test course.",
        )
        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Provider Event Course R1",
            summary="Published release for ProviderEvent testing.",
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

    def create_event(
        self,
        *,
        payment=None,
        provider="test-provider",
        merchant_reference=None,
        provider_transaction_id=None,
        amount_minor=None,
        currency=None,
        provider_status="raw-provider-status",
    ):
        if payment is None:
            payment = self.payment

        return ProviderEvent.objects.create(
            provider=provider,
            payment=payment,
            merchant_reference=(
                merchant_reference
                or self.payment.merchant_reference
            ),
            provider_event_id=f"event-{uuid.uuid4()}",
            provider_transaction_id=(
                provider_transaction_id
                or f"tx-{uuid.uuid4()}"
            ),
            event_type="payment-status",
            provider_status=provider_status,
            amount_minor=(
                self.payment.amount_minor
                if amount_minor is None
                else amount_minor
            ),
            currency=(
                self.payment.currency
                if currency is None
                else currency
            ),
            payload_digest=f"digest-{uuid.uuid4()}",
            authenticity_verified_at=timezone.now(),
            authenticity_method="test-signature",
        )

    def test_success_observation_updates_payment_and_fulfills(self):
        event = self.create_event()

        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()
        event.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.payment.provider_transaction_id,
            event.provider_transaction_id,
        )
        self.assertIsNotNone(self.payment.succeeded_at)

        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )

        self.assertTrue(
            CourseEntitlement.objects.filter(
                order=self.order,
                status=CourseEntitlement.Status.ACTIVE,
            ).exists()
        )
        self.assertTrue(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).exists()
        )

        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )
        self.assertEqual(event.attempt_count, 1)
        self.assertIsNotNone(event.processed_at)

    def test_reprocessing_same_event_is_idempotent(self):
        event = self.create_event()

        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )
        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        event.refresh_from_db()

        self.assertEqual(event.attempt_count, 1)
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

    def test_out_of_order_failure_does_not_regress_success(self):
        success_event = self.create_event()

        process_provider_event(
            provider_event=success_event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        late_failure = self.create_event(
            provider_transaction_id=(
                success_event.provider_transaction_id
            ),
            provider_status="late-failure",
        )

        process_provider_event(
            provider_event=late_failure,
            observed_payment_status=Payment.Status.FAILED,
        )

        self.payment.refresh_from_db()
        late_failure.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            late_failure.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )

    def test_late_success_on_closed_order_preserves_finance_fact(self):
        self.order.status = Order.Status.EXPIRED
        self.order.save(update_fields=["status"])

        event = self.create_event()

        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()
        event.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.order.status,
            Order.Status.EXPIRED,
        )

        self.assertFalse(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).exists()
        )
        self.assertFalse(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release__course=self.course,
            ).exists()
        )

        self.assertTrue(
            PaymentIntegrityCase.objects.filter(
                payment=self.payment,
                reason=(
                    PaymentIntegrityCase.Reason
                    .LATE_PAYMENT_CLOSED_ORDER
                ),
                status=PaymentIntegrityCase.Status.OPEN,
            ).exists()
        )

        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )

    def test_amount_mismatch_opens_case_without_payment_transition(self):
        event = self.create_event(
            amount_minor=self.payment.amount_minor + 1,
        )

        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        self.payment.refresh_from_db()
        event.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.CREATED,
        )

        self.assertTrue(
            PaymentIntegrityCase.objects.filter(
                payment=self.payment,
                provider_event=event,
                reason=PaymentIntegrityCase.Reason.AMOUNT_MISMATCH,
            ).exists()
        )

        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )

    def test_provider_identity_mismatch_opens_case(self):
        event = self.create_event(
            provider="different-provider",
        )

        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        self.payment.refresh_from_db()
        event.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.CREATED,
        )

        self.assertTrue(
            PaymentIntegrityCase.objects.filter(
                payment=self.payment,
                provider_event=event,
                reason=(
                    PaymentIntegrityCase.Reason
                    .PROVIDER_IDENTITY_MISMATCH
                ),
            ).exists()
        )

    def test_reconciliation_uses_same_payment_observation_path(self):
        apply_payment_observation(
            payment=self.payment,
            observed_status=Payment.Status.SUCCEEDED,
            provider_transaction_id="reconciliation-tx",
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.payment.provider_transaction_id,
            "reconciliation-tx",
        )
        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )

        self.assertTrue(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).exists()
        )

    def test_multiple_successful_payments_open_integrity_case(self):
        other_payment = Payment.objects.create(
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

        event = self.create_event()

        process_provider_event(
            provider_event=event,
            observed_payment_status=Payment.Status.SUCCEEDED,
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            other_payment.status,
            Payment.Status.SUCCEEDED,
        )

        self.assertTrue(
            PaymentIntegrityCase.objects.filter(
                order=self.order,
                payment=self.payment,
                reason=(
                    PaymentIntegrityCase.Reason
                    .MULTIPLE_SUCCESSFUL_PAYMENTS
                ),
            ).exists()
        )

        self.assertEqual(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).count(),
            1,
        )

class FinancialAdjustmentServiceTests(TestCase):
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="adjustment-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="adjustment-course",
            subject="Backend Engineering",
            title="Adjustment Course",
            summary="Financial adjustment correctness test course.",
        )
        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Adjustment Course R1",
            summary="Published release for adjustment testing.",
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
        fulfill_purchase(payment=self.payment)

    def create_adjustment(
        self,
        *,
        amount_minor,
        kind=FinancialAdjustment.Kind.REFUND,
        currency="IDR",
        status=FinancialAdjustment.Status.PENDING,
    ):
        return FinancialAdjustment.objects.create(
            payment=self.payment,
            kind=kind,
            status=status,
            amount_minor=amount_minor,
            currency=currency,
            operation_key=uuid.uuid4(),
            provider_reference=f"adj-{uuid.uuid4()}",
        )

    def test_partial_refund_preserves_purchase_access(self):
        adjustment = self.create_adjustment(
            amount_minor=200_000,
        )

        confirm_financial_adjustment(
            adjustment=adjustment,
        )

        adjustment.refresh_from_db()
        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )

        self.payment.refresh_from_db()

        self.assertEqual(
            adjustment.status,
            FinancialAdjustment.Status.CONFIRMED,
        )
        self.assertIsNotNone(adjustment.confirmed_at)

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )

        self.assertTrue(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).exists()
        )

    def test_cumulative_full_refund_revokes_purchase_entitlement(self):
        first = self.create_adjustment(
            amount_minor=200_000,
        )
        second = self.create_adjustment(
            amount_minor=300_000,
        )

        confirm_financial_adjustment(adjustment=first)
        confirm_financial_adjustment(adjustment=second)

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )
        self.payment.refresh_from_db()

        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.REVOKED,
        )
        self.assertIsNotNone(entitlement.revoked_at)

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )

        self.assertTrue(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).exists()
        )

    def test_full_chargeback_revokes_only_purchase_entitlement(self):
        scholarship = CourseEntitlement.objects.create(
            learner=self.learner,
            course=self.course,
            source=CourseEntitlement.Source.SCHOLARSHIP,
            status=CourseEntitlement.Status.ACTIVE,
            grant_reason="Test scholarship",
        )

        adjustment = self.create_adjustment(
            amount_minor=self.payment.amount_minor,
            kind=FinancialAdjustment.Kind.CHARGEBACK,
        )

        confirm_financial_adjustment(
            adjustment=adjustment,
        )

        purchase = CourseEntitlement.objects.get(
            order=self.order,
        )
        scholarship.refresh_from_db()

        self.assertEqual(
            purchase.status,
            CourseEntitlement.Status.REVOKED,
        )
        self.assertEqual(
            scholarship.status,
            CourseEntitlement.Status.ACTIVE,
        )

        self.assertTrue(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).exists()
        )

    def test_rejects_confirmed_total_above_acquired_amount(self):
        first = self.create_adjustment(
            amount_minor=300_000,
        )
        second = self.create_adjustment(
            amount_minor=300_000,
        )

        confirm_financial_adjustment(adjustment=first)

        with self.assertRaises(
            ExcessiveFinancialAdjustmentError
        ):
            confirm_financial_adjustment(
                adjustment=second,
            )

        second.refresh_from_db()

        self.assertEqual(
            second.status,
            FinancialAdjustment.Status.PENDING,
        )

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )

    def test_confirmation_retry_is_idempotent(self):
        adjustment = self.create_adjustment(
            amount_minor=200_000,
        )

        confirm_financial_adjustment(
            adjustment=adjustment,
        )
        confirm_financial_adjustment(
            adjustment=adjustment,
        )

        adjustment.refresh_from_db()

        confirmed_total = (
            FinancialAdjustment.objects.filter(
                payment=self.payment,
                status=FinancialAdjustment.Status.CONFIRMED,
            )
            .aggregate(total=models.Sum("amount_minor"))
            ["total"]
        )

        self.assertEqual(
            adjustment.status,
            FinancialAdjustment.Status.CONFIRMED,
        )
        self.assertEqual(confirmed_total, 200_000)

    def test_rejects_currency_mismatch(self):
        adjustment = self.create_adjustment(
            amount_minor=100_000,
            currency="USD",
        )

        with self.assertRaises(
            AdjustmentCurrencyMismatchError
        ):
            confirm_financial_adjustment(
                adjustment=adjustment,
            )

        adjustment.refresh_from_db()

        self.assertEqual(
            adjustment.status,
            FinancialAdjustment.Status.PENDING,
        )

    def test_failed_adjustment_cannot_be_confirmed(self):
        adjustment = self.create_adjustment(
            amount_minor=100_000,
            status=FinancialAdjustment.Status.FAILED,
        )

        with self.assertRaises(
            AdjustmentNotConfirmableError
        ):
            confirm_financial_adjustment(
                adjustment=adjustment,
            )
