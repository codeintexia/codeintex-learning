from datetime import timedelta
from hashlib import sha512
from unittest.mock import Mock

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from learning.models import Course, CourseRelease, Enrollment

from commerce.models import (
    CourseEntitlement,
    CourseOffer,
    FinancialAdjustment,
    Order,
    Payment,
    PaymentIntegrityCase,
    ProviderEvent,
)
from commerce.providers.midtrans import MidtransClient
from commerce.providers.midtrans_workflows import (
    MidtransNotificationAuthenticationError,
    ingest_midtrans_notification,
    process_midtrans_event,
    reconcile_midtrans_payment,
)
from commerce.services import (
    create_order,
    create_payment,
    fulfill_purchase,
)


class MidtransWorkflowTests(TestCase):
    server_key = "SB-Mid-server-test"

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="midtrans-workflow-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="midtrans-workflow-course",
            subject="Backend Engineering",
            title="Midtrans Workflow Course",
            summary="Midtrans workflow test course.",
        )
        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Midtrans Workflow Course R1",
            summary="Published release for Midtrans workflow testing.",
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
            provider="midtrans",
        )

    def signed_payload(
        self,
        *,
        transaction_status,
        transaction_id="midtrans-tx-1",
        gross_amount="500000.00",
        **extra,
    ):
        payload = {
            "order_id": self.payment.merchant_reference,
            "transaction_id": transaction_id,
            "transaction_status": transaction_status,
            "status_code": "200",
            "gross_amount": gross_amount,
            "currency": "IDR",
            **extra,
        }

        payload["signature_key"] = sha512(
            (
                payload["order_id"]
                + payload["status_code"]
                + payload["gross_amount"]
                + self.server_key
            ).encode("utf-8")
        ).hexdigest()

        return payload

    def mark_purchase_succeeded(self):
        self.payment.status = Payment.Status.SUCCEEDED
        self.payment.succeeded_at = timezone.now()
        self.payment.provider_transaction_id = "midtrans-tx-1"
        self.payment.save(
            update_fields=[
                "status",
                "succeeded_at",
                "provider_transaction_id",
            ]
        )
        fulfill_purchase(payment=self.payment)

    def test_ingest_only_persists_received_event(self):
        payload = self.signed_payload(
            transaction_status="settlement",
        )

        event = ingest_midtrans_notification(
            payload=payload,
            server_key=self.server_key,
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()

        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.RECEIVED,
        )
        self.assertEqual(
            self.payment.status,
            Payment.Status.CREATED,
        )
        self.assertEqual(
            self.order.status,
            Order.Status.OPEN,
        )
        self.assertFalse(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).exists()
        )

    def test_processing_success_event_fulfills_purchase(self):
        event = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="settlement",
            ),
            server_key=self.server_key,
        )

        process_midtrans_event(provider_event=event)

        self.payment.refresh_from_db()
        self.order.refresh_from_db()
        event.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )
        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )

        self.assertTrue(
            CourseEntitlement.objects.filter(
                order=self.order,
                status=CourseEntitlement.Status.ACTIVE,
            ).exists()
        )

    def test_invalid_signature_is_rejected_before_persistence(self):
        payload = self.signed_payload(
            transaction_status="settlement",
        )
        payload["signature_key"] = "invalid"

        with self.assertRaises(
            MidtransNotificationAuthenticationError
        ):
            ingest_midtrans_notification(
                payload=payload,
                server_key=self.server_key,
            )

        self.assertFalse(
            ProviderEvent.objects.filter(
                provider="midtrans",
            ).exists()
        )

    def test_duplicate_identical_notification_is_deduplicated(self):
        payload = self.signed_payload(
            transaction_status="settlement",
        )

        first = ingest_midtrans_notification(
            payload=payload,
            server_key=self.server_key,
        )
        second = ingest_midtrans_notification(
            payload=payload,
            server_key=self.server_key,
        )

        self.assertEqual(first.pk, second.pk)

        self.assertEqual(
            ProviderEvent.objects.filter(
                provider="midtrans",
            ).count(),
            1,
        )

        process_midtrans_event(provider_event=first)

        self.assertEqual(
            CourseEntitlement.objects.filter(
                order=self.order,
            ).count(),
            1,
        )

    def test_reconciliation_uses_existing_observation_engine(self):
        session = Mock()
        response = Mock()
        response.json.return_value = {
            "order_id": self.payment.merchant_reference,
            "transaction_id": "midtrans-tx-reconcile",
            "transaction_status": "settlement",
            "gross_amount": "500000.00",
            "currency": "IDR",
        }
        response.raise_for_status.return_value = None
        session.get.return_value = response

        client = MidtransClient(
            server_key=self.server_key,
            environment="sandbox",
            session=session,
        )

        reconcile_midtrans_payment(
            payment=self.payment,
            client=client,
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )

    def test_unconfirmed_refund_remains_pending(self):
        self.mark_purchase_succeeded()

        event = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="partial_refund",
                refund_amount="200000.00",
                refund_chargeback_id="refund-1",
            ),
            server_key=self.server_key,
        )

        process_midtrans_event(provider_event=event)

        adjustment = FinancialAdjustment.objects.get(
            payment=self.payment,
            provider_reference="refund-1",
        )

        self.assertEqual(
            adjustment.status,
            FinancialAdjustment.Status.PENDING,
        )

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )

    def test_cumulative_partial_refund_records_only_delta(self):
        self.mark_purchase_succeeded()

        first = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="partial_refund",
                refund_amount="200000.00",
                refund_chargeback_id="refund-1",
                bank_confirmed_at="2026-09-12 20:00:00",
            ),
            server_key=self.server_key,
        )
        second = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="partial_refund",
                refund_amount="300000.00",
                refund_chargeback_id="refund-2",
                bank_confirmed_at="2026-09-12 20:05:00",
            ),
            server_key=self.server_key,
        )

        process_midtrans_event(provider_event=first)
        process_midtrans_event(provider_event=second)

        adjustments = FinancialAdjustment.objects.filter(
            payment=self.payment,
            kind=FinancialAdjustment.Kind.REFUND,
            status=FinancialAdjustment.Status.CONFIRMED,
        ).order_by("created_at")

        self.assertEqual(
            list(
                adjustments.values_list(
                    "amount_minor",
                    flat=True,
                )
            ),
            [200_000, 100_000],
        )

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )

    def test_full_refund_revokes_purchase_but_preserves_enrollment(self):
        self.mark_purchase_succeeded()

        event = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="refund",
                refund_amount="500000.00",
                refund_chargeback_id="refund-full",
                bank_confirmed_at="2026-09-12 20:10:00",
            ),
            server_key=self.server_key,
        )

        process_midtrans_event(provider_event=event)

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )

        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.REVOKED,
        )

        self.assertTrue(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release=self.release,
            ).exists()
        )

    def test_deny_after_success_is_recorded_as_reversal(self):
        self.mark_purchase_succeeded()

        event = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="deny",
            ),
            server_key=self.server_key,
        )

        process_midtrans_event(provider_event=event)

        self.payment.refresh_from_db()

        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )

        reversal = FinancialAdjustment.objects.get(
            payment=self.payment,
            kind=FinancialAdjustment.Kind.REVERSAL,
        )

        self.assertEqual(
            reversal.status,
            FinancialAdjustment.Status.CONFIRMED,
        )
        self.assertEqual(
            reversal.amount_minor,
            self.payment.amount_minor,
        )

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.REVOKED,
        )

    def test_partial_chargeback_requires_integrity_review(self):
        self.mark_purchase_succeeded()

        event = ingest_midtrans_notification(
            payload=self.signed_payload(
                transaction_status="partial_chargeback",
            ),
            server_key=self.server_key,
        )

        process_midtrans_event(provider_event=event)

        entitlement = CourseEntitlement.objects.get(
            order=self.order,
        )

        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )

        self.assertTrue(
            PaymentIntegrityCase.objects.filter(
                payment=self.payment,
                reason=PaymentIntegrityCase.Reason.PARTIAL_CHARGEBACK,
                status=PaymentIntegrityCase.Status.OPEN,
            ).exists()
        )
