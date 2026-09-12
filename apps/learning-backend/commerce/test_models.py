import uuid
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.utils import timezone

from learning.models import Course

from .models import (
    CourseEntitlement,
    CourseOffer,
    FinancialAdjustment,
    Order,
    Payment,
    PaymentIntegrityCase,
    ProviderEvent,
)


class CommerceModelFixtureMixin:
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="commerce-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="commerce-test-course",
            subject="Backend Engineering",
            title="Commerce Test Course",
            summary="A course used by Commerce model tests.",
        )

    def create_offer(
        self,
        *,
        amount_minor=500_000,
        currency="IDR",
        is_active=True,
    ):
        return CourseOffer.objects.create(
            course=self.course,
            amount_minor=amount_minor,
            currency=currency,
            is_active=is_active,
        )

    def create_order(
        self,
        *,
        offer,
        subtotal_amount_minor=500_000,
        discount_amount_minor=0,
        total_amount_minor=500_000,
        status="OPEN",
    ):
        return Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=offer,
            status=status,
            subtotal_amount_minor=subtotal_amount_minor,
            discount_amount_minor=discount_amount_minor,
            total_amount_minor=total_amount_minor,
            currency="IDR",
            course_title_snapshot=self.course.title,
            expires_at=timezone.now() + timedelta(minutes=30),
        )


class CourseOfferConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def test_amount_must_be_greater_than_zero(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_offer(amount_minor=0)

    def test_only_one_active_offer_per_course_and_currency(self):
        self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_offer()

    def test_inactive_historical_offer_may_coexist(self):
        self.create_offer()

        historical = self.create_offer(
            amount_minor=400_000,
            is_active=False,
        )

        self.assertFalse(historical.is_active)


class OrderConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def test_only_one_open_order_per_learner_and_course(self):
        offer = self.create_offer()
        self.create_order(offer=offer)

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(offer=offer)

    def test_total_must_equal_subtotal_minus_discount(self):
        offer = self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(
                offer=offer,
                subtotal_amount_minor=500_000,
                discount_amount_minor=100_000,
                total_amount_minor=450_000,
            )

    def test_discount_must_not_exceed_subtotal(self):
        offer = self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(
                offer=offer,
                subtotal_amount_minor=500_000,
                discount_amount_minor=600_000,
                total_amount_minor=1,
            )

    def test_status_must_be_valid(self):
        offer = self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(
                offer=offer,
                status="INVALID",
            )

    def test_discount_must_not_exceed_subtotal(self):
        offer = self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(
                offer=offer,
                subtotal_amount_minor=500_000,
                discount_amount_minor=600_000,
                total_amount_minor=1,
            )

    def test_status_must_be_valid(self):
        offer = self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(
                offer=offer,
                status="INVALID",
            )

    def test_paid_purchase_total_must_be_greater_than_zero(self):
        offer = self.create_offer()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_order(
                offer=offer,
                subtotal_amount_minor=500_000,
                discount_amount_minor=500_000,
                total_amount_minor=0,
            )

class PaymentConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def setUp(self):
        super().setUp()
        self.offer = self.create_offer()
        self.order = self.create_order(offer=self.offer)

    def create_payment(
        self,
        *,
        status="CREATED",
        operation_key=None,
        merchant_reference=None,
        provider_transaction_id=None,
        amount_minor=500_000,
        provider="test-provider",
    ):
        return Payment.objects.create(
            order=self.order,
            provider=provider,
            status=status,
            operation_key=operation_key or uuid.uuid4(),
            merchant_reference=(
                merchant_reference
                or f"payment-{uuid.uuid4()}"
            ),
            provider_transaction_id=provider_transaction_id,
            amount_minor=amount_minor,
            currency="IDR",
        )

    def test_amount_must_be_greater_than_zero(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_payment(amount_minor=0)

    def test_operation_key_must_be_unique(self):
        operation_key = uuid.uuid4()
        self.create_payment(
            status="SUCCEEDED",
            operation_key=operation_key,
        )

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_payment(
                status="FAILED",
                operation_key=operation_key,
            )

    def test_merchant_reference_must_be_unique(self):
        merchant_reference = f"payment-{uuid.uuid4()}"
        self.create_payment(
            status="SUCCEEDED",
            merchant_reference=merchant_reference,
        )

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_payment(
                status="FAILED",
                merchant_reference=merchant_reference,
            )

    def test_provider_transaction_id_unique_within_provider(self):
        self.create_payment(
            status="SUCCEEDED",
            provider_transaction_id="provider-tx-1",
        )

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_payment(
                status="FAILED",
                provider_transaction_id="provider-tx-1",
            )

    def test_only_one_externally_payable_payment_per_order(self):
        self.create_payment(status="CREATED")

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_payment(status="PENDING")

    def test_status_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_payment(status="INVALID")

class ProviderEventConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def create_event(
        self,
        *,
        provider="test-provider",
        provider_event_id=None,
        processing_status="RECEIVED",
    ):
        return ProviderEvent.objects.create(
            provider=provider,
            provider_event_id=provider_event_id,
            merchant_reference=f"merchant-{uuid.uuid4()}",
            event_type="payment.updated",
            provider_status="settlement",
            payload_digest=f"digest-{uuid.uuid4()}",
            authenticity_verified_at=timezone.now(),
            authenticity_method="test-signature",
            processing_status=processing_status,
        )

    def test_provider_event_id_unique_within_provider(self):
        self.create_event(provider_event_id="event-1")

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_event(provider_event_id="event-1")

    def test_same_provider_event_id_may_exist_for_different_provider(self):
        self.create_event(
            provider="provider-a",
            provider_event_id="event-1",
        )

        event = self.create_event(
            provider="provider-b",
            provider_event_id="event-1",
        )

        self.assertEqual(event.provider, "provider-b")

    def test_null_provider_event_id_may_repeat(self):
        self.create_event()
        second = self.create_event()

        self.assertIsNone(second.provider_event_id)

    def test_processing_status_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_event(processing_status="INVALID")

class FinancialAdjustmentConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def setUp(self):
        super().setUp()
        self.offer = self.create_offer()
        self.order = self.create_order(offer=self.offer)
        self.payment = Payment.objects.create(
            order=self.order,
            provider="test-provider",
            status="SUCCEEDED",
            operation_key=uuid.uuid4(),
            merchant_reference=f"payment-{uuid.uuid4()}",
            provider_transaction_id=f"tx-{uuid.uuid4()}",
            amount_minor=500_000,
            currency="IDR",
            succeeded_at=timezone.now(),
        )

    def create_adjustment(
        self,
        *,
        payment=None,
        kind="REFUND",
        status="PENDING",
        amount_minor=100_000,
        operation_key=None,
        provider_reference=None,
    ):
        return FinancialAdjustment.objects.create(
            payment=payment or self.payment,
            kind=kind,
            status=status,
            amount_minor=amount_minor,
            currency="IDR",
            operation_key=operation_key,
            provider_reference=provider_reference,
            initiation_reason="test adjustment",
        )

    def test_amount_must_be_greater_than_zero(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_adjustment(amount_minor=0)

    def test_kind_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_adjustment(kind="INVALID")

    def test_status_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_adjustment(status="INVALID")

    def test_operation_key_unique_when_present(self):
        operation_key = uuid.uuid4()
        self.create_adjustment(operation_key=operation_key)

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_adjustment(operation_key=operation_key)

    def test_null_operation_key_may_repeat(self):
        self.create_adjustment()
        second = self.create_adjustment()

        self.assertIsNone(second.operation_key)

    def test_provider_reference_unique_within_payment(self):
        self.create_adjustment(provider_reference="refund-1")

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_adjustment(provider_reference="refund-1")

class PaymentIntegrityCaseConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def setUp(self):
        super().setUp()
        self.offer = self.create_offer()
        self.order = self.create_order(offer=self.offer)
        self.payment = Payment.objects.create(
            order=self.order,
            provider="test-provider",
            status="SUCCEEDED",
            operation_key=uuid.uuid4(),
            merchant_reference=f"payment-{uuid.uuid4()}",
            provider_transaction_id=f"tx-{uuid.uuid4()}",
            amount_minor=500_000,
            currency="IDR",
            succeeded_at=timezone.now(),
        )

    def create_case(
        self,
        *,
        case_key=None,
        reason="AMOUNT_MISMATCH",
        status="OPEN",
        order=None,
        payment=None,
        provider_event=None,
    ):
        return PaymentIntegrityCase.objects.create(
            order=self.order if order is None else order,
            payment=self.payment if payment is None else payment,
            provider_event=provider_event,
            case_key=case_key or f"case-{uuid.uuid4()}",
            reason=reason,
            status=status,
        )

    def test_case_key_must_be_unique(self):
        case_key = f"case-{uuid.uuid4()}"
        self.create_case(case_key=case_key)

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_case(case_key=case_key)

    def test_reason_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_case(reason="INVALID")

    def test_status_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_case(status="INVALID")

    def test_case_requires_at_least_one_reference(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            PaymentIntegrityCase.objects.create(
                case_key=f"case-{uuid.uuid4()}",
                reason="AMOUNT_MISMATCH",
                status="OPEN",
            )

class CourseEntitlementConstraintTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def setUp(self):
        super().setUp()
        self.offer = self.create_offer()
        self.order = self.create_order(offer=self.offer)

    def create_entitlement(
        self,
        *,
        source="PURCHASE",
        status="ACTIVE",
        order_marker="default",
    ):
        if order_marker == "default":
            order = self.order if source == "PURCHASE" else None
        else:
            order = order_marker

        return CourseEntitlement.objects.create(
            learner=self.learner,
            course=self.course,
            source=source,
            status=status,
            order=order,
            grant_reason="test entitlement",
        )

    def test_source_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_entitlement(
                source="INVALID",
                order_marker=None,
            )

    def test_status_must_be_valid(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_entitlement(status="INVALID")

    def test_purchase_requires_order(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_entitlement(
                source="PURCHASE",
                order_marker=None,
            )

    def test_non_purchase_source_must_not_reference_order(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_entitlement(
                source="SCHOLARSHIP",
                order_marker=self.order,
            )

    def test_order_may_back_at_most_one_entitlement(self):
        self.create_entitlement()

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_entitlement(status="REVOKED")

    def test_only_one_active_purchase_entitlement_per_course(self):
        self.create_entitlement()

        second_offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=600_000,
            currency="USD",
            is_active=True,
        )
        second_order = Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=second_offer,
            status="FULFILLED",
            subtotal_amount_minor=600_000,
            discount_amount_minor=0,
            total_amount_minor=600_000,
            currency="USD",
            course_title_snapshot=self.course.title,
            expires_at=timezone.now() + timedelta(minutes=30),
        )

        with self.assertRaises(IntegrityError), transaction.atomic():
            self.create_entitlement(
                order_marker=second_order,
            )

    def test_revoked_purchase_allows_new_active_purchase(self):
        first = self.create_entitlement(status="REVOKED")

        second_offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=600_000,
            currency="USD",
            is_active=True,
        )
        second_order = Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=second_offer,
            status="FULFILLED",
            subtotal_amount_minor=600_000,
            discount_amount_minor=0,
            total_amount_minor=600_000,
            currency="USD",
            course_title_snapshot=self.course.title,
            expires_at=timezone.now() + timedelta(minutes=30),
        )

        second = self.create_entitlement(
            order_marker=second_order,
        )

        self.assertEqual(first.status, "REVOKED")
        self.assertEqual(second.status, "ACTIVE")

    def test_independent_grants_may_coexist(self):
        scholarship = self.create_entitlement(
            source="SCHOLARSHIP",
        )
        admin_grant = self.create_entitlement(
            source="ADMIN_GRANT",
        )

        self.assertEqual(scholarship.status, "ACTIVE")
        self.assertEqual(admin_grant.status, "ACTIVE")



class CommerceImmutabilityTests(
    CommerceModelFixtureMixin,
    TestCase,
):
    def test_course_offer_commercial_identity_is_immutable(self):
        offer = self.create_offer()

        offer.amount_minor = 600_000

        with self.assertRaises(ValueError):
            offer.save()

    def test_order_commercial_snapshot_is_immutable(self):
        offer = self.create_offer()
        order = self.create_order(offer=offer)

        order.total_amount_minor = 400_000

        with self.assertRaises(ValueError):
            order.save()
