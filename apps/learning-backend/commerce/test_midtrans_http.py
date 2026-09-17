import json
from datetime import timedelta
from hashlib import sha512

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.utils import timezone

from learning.models import Course, CourseRelease, Enrollment

from commerce.models import (
    CourseEntitlement,
    CourseOffer,
    Order,
    Payment,
    ProviderEvent,
)
from commerce.services import create_order, create_payment


@override_settings(
    MIDTRANS_SERVER_KEY="SB-Mid-server-http-test",
)
class MidtransNotificationHttpTests(TestCase):
    endpoint = "/api/v1/commerce/providers/midtrans/notifications/"
    server_key = "SB-Mid-server-http-test"

    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="midtrans-http-learner",
            password="test-password",
        )

        self.course = Course.objects.create(
            slug="midtrans-http-course",
            subject="Backend Engineering",
            title="Midtrans HTTP Course",
            summary="Midtrans HTTP ingress test course.",
        )

        CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Midtrans HTTP Course R1",
            summary="Published release for HTTP ingress testing.",
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

    def signed_payload(self):
        payload = {
            "order_id": self.payment.merchant_reference,
            "transaction_id": "midtrans-http-tx-1",
            "transaction_status": "settlement",
            "status_code": "200",
            "gross_amount": "500000.00",
            "currency": "IDR",
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

    def test_valid_notification_is_ingested_and_processed(self):
        response = self.client.post(
            self.endpoint,
            data=json.dumps(self.signed_payload()),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)

        event = ProviderEvent.objects.get(
            provider="midtrans",
            merchant_reference=self.payment.merchant_reference,
        )

        self.payment.refresh_from_db()
        self.order.refresh_from_db()

        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )
        self.assertEqual(event.attempt_count, 1)
        self.assertEqual(
            self.payment.status,
            Payment.Status.SUCCEEDED,
        )
        self.assertEqual(
            self.order.status,
            Order.Status.FULFILLED,
        )

        entitlement = CourseEntitlement.objects.get(
            learner=self.learner,
            course=self.course,
        )
        self.assertEqual(
            entitlement.source,
            CourseEntitlement.Source.PURCHASE,
        )
        self.assertEqual(
            entitlement.status,
            CourseEntitlement.Status.ACTIVE,
        )

        self.assertEqual(
            Enrollment.objects.filter(
                learner=self.learner,
                course_release__course=self.course,
            ).count(),
            1,
        )

    def test_replayed_valid_notification_is_idempotent(self):
        payload = self.signed_payload()

        first = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type="application/json",
        )
        second = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(first.status_code, 200)
        self.assertEqual(second.status_code, 200)

        events = ProviderEvent.objects.filter(
            provider="midtrans",
            merchant_reference=self.payment.merchant_reference,
        )

        self.assertEqual(events.count(), 1)

        event = events.get()

        self.assertEqual(
            event.processing_status,
            ProviderEvent.ProcessingStatus.PROCESSED,
        )
        self.assertEqual(event.attempt_count, 1)

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

        self.assertEqual(
            CourseEntitlement.objects.filter(
                learner=self.learner,
                course=self.course,
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

    def test_invalid_signature_is_rejected_without_persistence(self):
        payload = self.signed_payload()
        payload["signature_key"] = "invalid"

        response = self.client.post(
            self.endpoint,
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 401)
        self.assertFalse(
            ProviderEvent.objects.filter(
                provider="midtrans",
            ).exists()
        )

    def test_malformed_json_is_rejected(self):
        response = self.client.post(
            self.endpoint,
            data="{not-json",
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(
            ProviderEvent.objects.filter(
                provider="midtrans",
            ).exists()
        )
