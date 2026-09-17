from unittest.mock import Mock, patch

from django.contrib.auth import get_user_model
from django.test import Client, TestCase, override_settings

from learning.models import Course, CourseRelease

from commerce.models import (
    CourseEntitlement,
    CourseOffer,
    Order,
    Payment,
)
from commerce.providers.midtrans import (
    MidtransCheckout,
    MidtransProtocolError,
)


CHECKOUT_URL = "/api/v1/commerce/courses/checkout-course/checkout/"
OFFER_URL = "/api/v1/commerce/courses/checkout-course/offer/"


@override_settings(
    MIDTRANS_SERVER_KEY="SB-Mid-server-test",
    MIDTRANS_ENVIRONMENT="sandbox",
)
class CheckoutHttpTests(TestCase):
    def setUp(self):
        self.learner = get_user_model().objects.create_user(
            username="checkout-learner",
            password="test-password",
        )
        self.course = Course.objects.create(
            slug="checkout-course",
            subject="Backend Engineering",
            title="Checkout Course",
            summary="Checkout HTTP contract course.",
        )
        self.release = CourseRelease.objects.create(
            course=self.course,
            release_number=1,
            title="Checkout Course",
            summary="Published checkout release.",
            is_published=True,
        )
        self.offer = CourseOffer.objects.create(
            course=self.course,
            amount_minor=500_000,
            currency="IDR",
            is_active=True,
        )

    def test_checkout_requires_authentication(self):
        response = self.client.post(CHECKOUT_URL)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)

    def test_checkout_is_csrf_protected(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.learner)

        response = client.post(CHECKOUT_URL)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)

    @patch("commerce.http_api.MidtransClient", create=True)
    def test_checkout_uses_server_authoritative_offer_and_persists_capability(
        self,
        client_class,
    ):
        self.client.force_login(self.learner)

        provider_client = Mock()
        provider_client.create_snap_checkout.return_value = MidtransCheckout(
            token="snap-token-123",
            redirect_url=(
                "https://app.sandbox.midtrans.com/"
                "snap/v2/vtweb/snap-token-123"
            ),
        )
        client_class.return_value = provider_client

        response = self.client.post(
            CHECKOUT_URL,
            data={
                "amountMinor": 1,
                "currency": "USD",
                "offerId": "not-authoritative",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)

        order = Order.objects.get()
        payment = Payment.objects.get()

        self.assertEqual(order.learner, self.learner)
        self.assertEqual(order.course, self.course)
        self.assertEqual(order.offer, self.offer)
        self.assertEqual(order.total_amount_minor, 500_000)
        self.assertEqual(order.currency, "IDR")

        self.assertEqual(payment.order, order)
        self.assertEqual(payment.amount_minor, 500_000)
        self.assertEqual(payment.currency, "IDR")
        self.assertEqual(
            payment.checkout_url,
            (
                "https://app.sandbox.midtrans.com/"
                "snap/v2/vtweb/snap-token-123"
            ),
        )

        provider_client.create_snap_checkout.assert_called_once_with(
            merchant_reference=payment.merchant_reference,
            amount_minor=500_000,
            currency="IDR",
            idempotency_key=str(payment.operation_key),
        )

        payload = response.json()["checkout"]
        self.assertEqual(payload["paymentId"], str(payment.pk))
        self.assertEqual(payload["orderId"], str(order.pk))
        self.assertEqual(payload["redirectUrl"], payment.checkout_url)
        self.assertEqual(payload["amountMinor"], 500_000)
        self.assertEqual(payload["currency"], "IDR")
        self.assertIn("expiresAt", payload)

    @override_settings(
        MIDTRANS_NOTIFICATION_URL=(
            "https://notify.example.test/"
            "api/v1/commerce/providers/midtrans/notifications/"
        ),
    )
    @patch("commerce.http_api.MidtransClient", create=True)
    def test_checkout_passes_configured_notification_url_to_provider(
        self,
        client_class,
    ):
        self.client.force_login(self.learner)

        provider_client = Mock()
        provider_client.create_snap_checkout.return_value = MidtransCheckout(
            token="snap-token-123",
            redirect_url="https://example.test/snap-token-123",
        )
        client_class.return_value = provider_client

        response = self.client.post(CHECKOUT_URL)

        self.assertEqual(response.status_code, 201)

        payment = Payment.objects.get()

        provider_client.create_snap_checkout.assert_called_once_with(
            merchant_reference=payment.merchant_reference,
            amount_minor=500_000,
            currency="IDR",
            idempotency_key=str(payment.operation_key),
            notification_url=(
                "https://notify.example.test/"
                "api/v1/commerce/providers/midtrans/notifications/"
            ),
        )

    @patch("commerce.http_api.MidtransClient", create=True)
    def test_checkout_retry_reuses_order_payment_and_checkout_url(
        self,
        client_class,
    ):
        self.client.force_login(self.learner)

        provider_client = Mock()
        provider_client.create_snap_checkout.return_value = MidtransCheckout(
            token="snap-token-123",
            redirect_url="https://example.test/snap-token-123",
        )
        client_class.return_value = provider_client

        first = self.client.post(CHECKOUT_URL)
        second = self.client.post(CHECKOUT_URL)

        self.assertEqual(first.status_code, 201)
        self.assertEqual(second.status_code, 200)

        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Payment.objects.count(), 1)

        payment = Payment.objects.get()

        self.assertEqual(
            first.json()["checkout"]["paymentId"],
            second.json()["checkout"]["paymentId"],
        )
        self.assertEqual(
            second.json()["checkout"]["redirectUrl"],
            payment.checkout_url,
        )
        provider_client.create_snap_checkout.assert_called_once()

    @patch("commerce.http_api.MidtransClient", create=True)
    def test_checkout_rejects_learner_with_active_purchase_entitlement(
        self,
        client_class,
    ):
        self.client.force_login(self.learner)

        order = Order.objects.create(
            learner=self.learner,
            course=self.course,
            offer=self.offer,
            status=Order.Status.FULFILLED,
            subtotal_amount_minor=500_000,
            discount_amount_minor=0,
            total_amount_minor=500_000,
            currency="IDR",
            course_title_snapshot=self.course.title,
            expires_at=self.offer.created_at,
            fulfilled_at=self.offer.created_at,
        )
        CourseEntitlement.objects.create(
            learner=self.learner,
            course=self.course,
            source=CourseEntitlement.Source.PURCHASE,
            status=CourseEntitlement.Status.ACTIVE,
            order=order,
            grant_reason="Existing purchase",
        )

        response = self.client.post(CHECKOUT_URL)

        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()["error"], "already_entitled")
        client_class.assert_not_called()

    def test_checkout_rejects_course_without_published_release(self):
        self.client.force_login(self.learner)

        unavailable_course = Course.objects.create(
            slug="unreleased-course",
            subject="Backend Engineering",
            title="Unreleased Course",
            summary="Not yet sellable.",
        )
        CourseOffer.objects.create(
            course=unavailable_course,
            amount_minor=250_000,
            currency="IDR",
            is_active=True,
        )

        response = self.client.post(
            "/api/v1/commerce/courses/unreleased-course/checkout/"
        )

        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            response.json()["error"],
            "course_unavailable",
        )
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)

    @patch("commerce.http_api.MidtransClient", create=True)
    def test_checkout_retry_after_provider_error_reuses_local_payment(
        self,
        client_class,
    ):
        self.client.force_login(self.learner)

        provider_client = Mock()
        provider_client.create_snap_checkout.side_effect = (
            MidtransProtocolError("provider unavailable")
        )
        client_class.return_value = provider_client

        first = self.client.post(CHECKOUT_URL)

        self.assertEqual(first.status_code, 502)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Payment.objects.count(), 1)

        order_id = Order.objects.get().pk
        payment_id = Payment.objects.get().pk

        provider_client.create_snap_checkout.side_effect = None
        provider_client.create_snap_checkout.return_value = MidtransCheckout(
            token="retry-token",
            redirect_url="https://example.test/retry-token",
        )

        second = self.client.post(CHECKOUT_URL)

        self.assertEqual(second.status_code, 200)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Order.objects.get().pk, order_id)
        self.assertEqual(Payment.objects.get().pk, payment_id)
        self.assertEqual(
            second.json()["checkout"]["redirectUrl"],
            "https://example.test/retry-token",
        )

    def test_checkout_returns_not_found_for_unknown_course(self):
        self.client.force_login(self.learner)

        response = self.client.post(
            "/api/v1/commerce/courses/missing-course/checkout/"
        )

        self.assertEqual(response.status_code, 404)

    @override_settings(MIDTRANS_SERVER_KEY="")
    def test_checkout_fails_closed_when_provider_is_not_configured(self):
        self.client.force_login(self.learner)

        response = self.client.post(CHECKOUT_URL)

        self.assertEqual(response.status_code, 503)
        self.assertEqual(
            response.json()["error"],
            "payment_provider_unavailable",
        )
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)

    def test_offer_is_public_and_returns_active_server_offer(self):
        response = self.client.get(OFFER_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "offer": {
                    "amountMinor": 500_000,
                    "currency": "IDR",
                }
            },
        )
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)

    def test_offer_returns_unavailable_when_no_active_offer_exists(self):
        self.offer.is_active = False
        self.offer.save(update_fields=["is_active"])

        response = self.client.get(OFFER_URL)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["error"],
            "offer_unavailable",
        )
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)

    def test_offer_hides_course_without_published_release(self):
        unavailable_course = Course.objects.create(
            slug="unreleased-offer-course",
            subject="Backend Engineering",
            title="Unreleased Offer Course",
            summary="Not published.",
        )
        CourseOffer.objects.create(
            course=unavailable_course,
            amount_minor=250_000,
            currency="IDR",
            is_active=True,
        )

        response = self.client.get(
            "/api/v1/commerce/courses/"
            "unreleased-offer-course/offer/"
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json()["error"],
            "course_unavailable",
        )
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Payment.objects.count(), 0)
