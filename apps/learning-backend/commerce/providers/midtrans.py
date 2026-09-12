from dataclasses import dataclass
from hashlib import sha512
from hmac import compare_digest
from typing import Any

import requests

from commerce.models import FinancialAdjustment, Payment


class MidtransError(Exception):
    """Base error for the Midtrans adapter."""


class MidtransConfigurationError(MidtransError):
    """Raised when the adapter configuration is invalid."""


class MidtransProtocolError(MidtransError):
    """Raised when Midtrans returns an unsupported or invalid payload."""


@dataclass(frozen=True)
class MidtransCheckout:
    token: str
    redirect_url: str


@dataclass(frozen=True)
class MidtransObservation:
    payment_status: str
    adjustment_kind: str | None = None
    is_partial_adjustment: bool = False


class MidtransClient:
    TIMEOUT = (3.05, 10.0)

    SNAP_BASE_URLS = {
        "sandbox": "https://app.sandbox.midtrans.com",
        "production": "https://app.midtrans.com",
    }

    API_BASE_URLS = {
        "sandbox": "https://api.sandbox.midtrans.com",
        "production": "https://api.midtrans.com",
    }

    def __init__(
        self,
        *,
        server_key: str,
        environment: str,
        session=None,
    ):
        if environment not in self.SNAP_BASE_URLS:
            raise MidtransConfigurationError(
                "Midtrans environment must be 'sandbox' or 'production'."
            )

        if not server_key:
            raise MidtransConfigurationError(
                "Midtrans Server Key is required."
            )

        self.server_key = server_key
        self.environment = environment
        self.session = session or requests.Session()

    def create_snap_checkout(
        self,
        *,
        merchant_reference: str,
        amount_minor: int,
        currency: str,
    ) -> MidtransCheckout:
        if currency != "IDR":
            raise MidtransConfigurationError(
                "Midtrans Snap V1 checkout currently requires IDR."
            )

        if not merchant_reference:
            raise MidtransConfigurationError(
                "merchant_reference is required."
            )

        if len(merchant_reference) > 50:
            raise MidtransConfigurationError(
                "Midtrans order_id cannot exceed 50 characters."
            )

        if amount_minor <= 0:
            raise MidtransConfigurationError(
                "Midtrans gross_amount must be greater than zero."
            )

        response = self.session.post(
            (
                f"{self.SNAP_BASE_URLS[self.environment]}"
                "/snap/v1/transactions"
            ),
            json={
                "transaction_details": {
                    "order_id": merchant_reference,
                    "gross_amount": amount_minor,
                },
            },
            auth=(self.server_key, ""),
            headers={"Accept": "application/json"},
            timeout=self.TIMEOUT,
        )

        response.raise_for_status()
        payload = response.json()

        token = payload.get("token")
        redirect_url = payload.get("redirect_url")

        if not token or not redirect_url:
            raise MidtransProtocolError(
                "Midtrans Snap response is missing token or redirect_url."
            )

        return MidtransCheckout(
            token=token,
            redirect_url=redirect_url,
        )

    def get_transaction_status(
        self,
        *,
        merchant_reference: str,
    ) -> dict[str, Any]:
        if not merchant_reference:
            raise MidtransConfigurationError(
                "merchant_reference is required."
            )

        response = self.session.get(
            (
                f"{self.API_BASE_URLS[self.environment]}"
                f"/v2/{merchant_reference}/status"
            ),
            auth=(self.server_key, ""),
            headers={"Accept": "application/json"},
            timeout=self.TIMEOUT,
        )

        response.raise_for_status()
        payload = response.json()

        if not isinstance(payload, dict):
            raise MidtransProtocolError(
                "Midtrans status response must be a JSON object."
            )

        return payload

    def normalize_transaction(
        self,
        payload: dict[str, Any],
    ) -> MidtransObservation:
        transaction_status = payload.get("transaction_status")

        if transaction_status == "pending":
            return MidtransObservation(
                payment_status=Payment.Status.PENDING,
            )

        if transaction_status == "authorize":
            return MidtransObservation(
                payment_status=Payment.Status.PENDING,
            )

        if transaction_status == "capture":
            fraud_status = payload.get("fraud_status")

            if fraud_status == "accept":
                return MidtransObservation(
                    payment_status=Payment.Status.SUCCEEDED,
                )

            return MidtransObservation(
                payment_status=Payment.Status.PENDING,
            )

        if transaction_status == "settlement":
            return MidtransObservation(
                payment_status=Payment.Status.SUCCEEDED,
            )

        if transaction_status in {"deny", "failure"}:
            return MidtransObservation(
                payment_status=Payment.Status.FAILED,
            )

        if transaction_status == "cancel":
            return MidtransObservation(
                payment_status=Payment.Status.CANCELLED,
            )

        if transaction_status == "expire":
            return MidtransObservation(
                payment_status=Payment.Status.EXPIRED,
            )

        if transaction_status == "refund":
            return MidtransObservation(
                payment_status=Payment.Status.SUCCEEDED,
                adjustment_kind=FinancialAdjustment.Kind.REFUND,
            )

        if transaction_status == "partial_refund":
            return MidtransObservation(
                payment_status=Payment.Status.SUCCEEDED,
                adjustment_kind=FinancialAdjustment.Kind.REFUND,
                is_partial_adjustment=True,
            )

        if transaction_status == "chargeback":
            return MidtransObservation(
                payment_status=Payment.Status.SUCCEEDED,
                adjustment_kind=FinancialAdjustment.Kind.CHARGEBACK,
            )

        if transaction_status == "partial_chargeback":
            return MidtransObservation(
                payment_status=Payment.Status.SUCCEEDED,
                adjustment_kind=FinancialAdjustment.Kind.CHARGEBACK,
                is_partial_adjustment=True,
            )

        raise MidtransProtocolError(
            f"Unsupported Midtrans transaction_status: "
            f"{transaction_status!r}"
        )


def verify_notification_signature(
    *,
    payload: dict[str, Any],
    server_key: str,
) -> bool:
    try:
        order_id = str(payload["order_id"])
        status_code = str(payload["status_code"])
        gross_amount = str(payload["gross_amount"])
        signature_key = str(payload["signature_key"])
    except (KeyError, TypeError):
        return False

    expected_signature = sha512(
        (
            order_id
            + status_code
            + gross_amount
            + server_key
        ).encode("utf-8")
    ).hexdigest()

    return compare_digest(
        signature_key,
        expected_signature,
    )
