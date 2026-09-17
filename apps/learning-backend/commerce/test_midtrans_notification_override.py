from unittest.mock import Mock

from django.test import SimpleTestCase

from commerce.providers.midtrans import MidtransClient


class MidtransNotificationOverrideTests(SimpleTestCase):
    def _client(self):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {
            "token": "sandbox-token",
            "redirect_url": "https://app.sandbox.midtrans.com/example",
        }

        session = Mock()
        session.post.return_value = response

        return (
            MidtransClient(
                server_key="sandbox-server-key",
                environment="sandbox",
                session=session,
            ),
            session,
        )

    def test_create_snap_checkout_sends_override_notification_header(self):
        client, session = self._client()

        client.create_snap_checkout(
            merchant_reference="payment-test",
            amount_minor=10_000,
            currency="IDR",
            idempotency_key="operation-test",
            notification_url=(
                "https://example.test/"
                "api/v1/commerce/providers/midtrans/notifications/"
            ),
        )

        headers = session.post.call_args.kwargs["headers"]

        self.assertEqual(
            headers["X-Override-Notification"],
            (
                "https://example.test/"
                "api/v1/commerce/providers/midtrans/notifications/"
            ),
        )
        self.assertEqual(
            headers["Idempotency-Key"],
            "operation-test",
        )

    def test_create_snap_checkout_omits_override_when_unconfigured(self):
        client, session = self._client()

        client.create_snap_checkout(
            merchant_reference="payment-test",
            amount_minor=10_000,
            currency="IDR",
        )

        headers = session.post.call_args.kwargs["headers"]

        self.assertNotIn(
            "X-Override-Notification",
            headers,
        )
