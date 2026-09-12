from hashlib import sha512
from unittest.mock import Mock

from django.test import SimpleTestCase

from commerce.models import FinancialAdjustment, Payment
from commerce.providers.midtrans import (
    MidtransClient,
    MidtransConfigurationError,
    MidtransObservation,
    verify_notification_signature,
)


class MidtransAdapterTests(SimpleTestCase):
    def make_response(self, *, status_code=200, payload=None):
        response = Mock()
        response.status_code = status_code
        response.json.return_value = payload or {}
        return response

    def test_create_snap_checkout_uses_server_authoritative_payment_data(self):
        session = Mock()
        session.post.return_value = self.make_response(
            status_code=201,
            payload={
                "token": "snap-token-123",
                "redirect_url": (
                    "https://app.sandbox.midtrans.com/"
                    "snap/v2/vtweb/snap-token-123"
                ),
            },
        )

        client = MidtransClient(
            server_key="SB-Mid-server-test",
            environment="sandbox",
            session=session,
        )

        checkout = client.create_snap_checkout(
            merchant_reference="payment-123",
            amount_minor=500_000,
            currency="IDR",
        )

        self.assertEqual(checkout.token, "snap-token-123")
        self.assertIn("snap-token-123", checkout.redirect_url)

        session.post.assert_called_once_with(
            (
                "https://app.sandbox.midtrans.com/"
                "snap/v1/transactions"
            ),
            json={
                "transaction_details": {
                    "order_id": "payment-123",
                    "gross_amount": 500_000,
                },
            },
            auth=("SB-Mid-server-test", ""),
            headers={"Accept": "application/json"},
            timeout=(3.05, 10.0),
        )

    def test_create_checkout_rejects_non_idr_currency(self):
        client = MidtransClient(
            server_key="SB-Mid-server-test",
            environment="sandbox",
            session=Mock(),
        )

        with self.assertRaises(MidtransConfigurationError):
            client.create_snap_checkout(
                merchant_reference="payment-123",
                amount_minor=500_000,
                currency="USD",
            )

    def test_production_uses_production_snap_endpoint(self):
        session = Mock()
        session.post.return_value = self.make_response(
            status_code=201,
            payload={
                "token": "production-token",
                "redirect_url": (
                    "https://app.midtrans.com/"
                    "snap/v2/vtweb/production-token"
                ),
            },
        )

        client = MidtransClient(
            server_key="Mid-server-production",
            environment="production",
            session=session,
        )

        client.create_snap_checkout(
            merchant_reference="payment-456",
            amount_minor=750_000,
            currency="IDR",
        )

        self.assertEqual(
            session.post.call_args.args[0],
            "https://app.midtrans.com/snap/v1/transactions",
        )

    def test_notification_signature_uses_exact_midtrans_fields(self):
        server_key = "SB-Mid-server-secret"
        payload = {
            "order_id": "payment-123",
            "status_code": "200",
            "gross_amount": "500000.00",
        }

        expected = sha512(
            (
                "payment-123"
                "200"
                "500000.00"
                + server_key
            ).encode("utf-8")
        ).hexdigest()

        payload["signature_key"] = expected

        self.assertTrue(
            verify_notification_signature(
                payload=payload,
                server_key=server_key,
            )
        )

        payload["signature_key"] = "invalid"

        self.assertFalse(
            verify_notification_signature(
                payload=payload,
                server_key=server_key,
            )
        )

    def test_normalizes_midtrans_payment_status_matrix(self):
        client = MidtransClient(
            server_key="SB-Mid-server-test",
            environment="sandbox",
            session=Mock(),
        )

        cases = [
            (
                {"transaction_status": "pending"},
                MidtransObservation(
                    payment_status=Payment.Status.PENDING,
                ),
            ),
            (
                {
                    "transaction_status": "capture",
                    "fraud_status": "accept",
                },
                MidtransObservation(
                    payment_status=Payment.Status.SUCCEEDED,
                ),
            ),
            (
                {
                    "transaction_status": "capture",
                    "fraud_status": "challenge",
                },
                MidtransObservation(
                    payment_status=Payment.Status.PENDING,
                ),
            ),
            (
                {"transaction_status": "settlement"},
                MidtransObservation(
                    payment_status=Payment.Status.SUCCEEDED,
                ),
            ),
            (
                {"transaction_status": "deny"},
                MidtransObservation(
                    payment_status=Payment.Status.FAILED,
                ),
            ),
            (
                {"transaction_status": "failure"},
                MidtransObservation(
                    payment_status=Payment.Status.FAILED,
                ),
            ),
            (
                {"transaction_status": "cancel"},
                MidtransObservation(
                    payment_status=Payment.Status.CANCELLED,
                ),
            ),
            (
                {"transaction_status": "expire"},
                MidtransObservation(
                    payment_status=Payment.Status.EXPIRED,
                ),
            ),
            (
                {"transaction_status": "authorize"},
                MidtransObservation(
                    payment_status=Payment.Status.PENDING,
                ),
            ),
        ]

        for payload, expected in cases:
            with self.subTest(payload=payload):
                self.assertEqual(
                    client.normalize_transaction(payload),
                    expected,
                )

    def test_refund_and_chargeback_preserve_acquisition_success(self):
        client = MidtransClient(
            server_key="SB-Mid-server-test",
            environment="sandbox",
            session=Mock(),
        )

        cases = [
            (
                "refund",
                FinancialAdjustment.Kind.REFUND,
                False,
            ),
            (
                "partial_refund",
                FinancialAdjustment.Kind.REFUND,
                True,
            ),
            (
                "chargeback",
                FinancialAdjustment.Kind.CHARGEBACK,
                False,
            ),
            (
                "partial_chargeback",
                FinancialAdjustment.Kind.CHARGEBACK,
                True,
            ),
        ]

        for raw_status, kind, is_partial in cases:
            with self.subTest(raw_status=raw_status):
                observation = client.normalize_transaction(
                    {"transaction_status": raw_status}
                )

                self.assertEqual(
                    observation.payment_status,
                    Payment.Status.SUCCEEDED,
                )
                self.assertEqual(
                    observation.adjustment_kind,
                    kind,
                )
                self.assertEqual(
                    observation.is_partial_adjustment,
                    is_partial,
                )

    def test_get_transaction_status_uses_core_status_api(self):
        session = Mock()
        session.get.return_value = self.make_response(
            payload={
                "order_id": "payment-123",
                "transaction_status": "settlement",
                "transaction_id": "midtrans-tx-123",
                "gross_amount": "500000.00",
            },
        )

        client = MidtransClient(
            server_key="SB-Mid-server-test",
            environment="sandbox",
            session=session,
        )

        payload = client.get_transaction_status(
            merchant_reference="payment-123",
        )

        self.assertEqual(
            payload["transaction_status"],
            "settlement",
        )

        session.get.assert_called_once_with(
            (
                "https://api.sandbox.midtrans.com/"
                "v2/payment-123/status"
            ),
            auth=("SB-Mid-server-test", ""),
            headers={"Accept": "application/json"},
            timeout=(3.05, 10.0),
        )

    def test_invalid_environment_is_rejected(self):
        with self.assertRaises(MidtransConfigurationError):
            MidtransClient(
                server_key="test-key",
                environment="staging",
                session=Mock(),
            )
