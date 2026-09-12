import json
from decimal import Decimal, InvalidOperation
from hashlib import sha256

from django.db import transaction
from django.db.models import Sum
from django.utils import timezone

from commerce.models import (
    FinancialAdjustment,
    Payment,
    PaymentIntegrityCase,
    ProviderEvent,
)
from commerce.providers.midtrans import (
    MidtransClient,
    MidtransProtocolError,
    verify_notification_signature,
)
from commerce.services import (
    apply_payment_observation,
    confirm_financial_adjustment,
    process_provider_event,
)


class MidtransNotificationAuthenticationError(Exception):
    """Raised when a Midtrans notification cannot be authenticated."""


def _amount_minor(value) -> int | None:
    if value in (None, ""):
        return None

    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise MidtransProtocolError(
            f"Invalid Midtrans amount: {value!r}"
        ) from exc

    integral = amount.to_integral_value()

    if amount != integral or integral < 0:
        raise MidtransProtocolError(
            f"Midtrans amount must be a non-negative IDR integer: {value!r}"
        )

    return int(integral)


def _payload_digest(payload: dict) -> str:
    canonical = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        default=str,
    ).encode("utf-8")

    return sha256(canonical).hexdigest()


def _normalized_evidence(
    *,
    payload: dict,
    server_key: str,
) -> dict:
    client = MidtransClient(
        server_key=server_key,
        environment="sandbox",
    )

    try:
        observation = client.normalize_transaction(payload)
    except MidtransProtocolError:
        observation = None

    transaction_status = str(
        payload.get("transaction_status", "")
    )

    cumulative_amount = None
    provider_adjustment_reference = None
    adjustment_confirmed = False
    adjustment_kind = None
    is_partial = False
    observed_payment_status = None

    if observation is not None:
        observed_payment_status = observation.payment_status
        adjustment_kind = observation.adjustment_kind
        is_partial = observation.is_partial_adjustment

    if adjustment_kind is not None:
        cumulative_amount = _amount_minor(
            payload.get("refund_amount")
        )
        provider_adjustment_reference = payload.get(
            "refund_chargeback_id"
        )
        if provider_adjustment_reference is not None:
            provider_adjustment_reference = str(
                provider_adjustment_reference
            )

        adjustment_confirmed = bool(
            payload.get("bank_confirmed_at")
        )

    return {
        "provider_status": transaction_status,
        "observed_payment_status": observed_payment_status,
        "adjustment_kind": adjustment_kind,
        "adjustment_cumulative_amount_minor": cumulative_amount,
        "provider_adjustment_reference": provider_adjustment_reference,
        "adjustment_confirmed": adjustment_confirmed,
        "is_partial_adjustment": is_partial,
    }


@transaction.atomic
def _persist_authenticated_midtrans_event(
    *,
    payload: dict,
    server_key: str,
    authenticity_method: str,
) -> ProviderEvent:
    merchant_reference = str(payload.get("order_id", ""))
    provider_transaction_id = payload.get("transaction_id")

    if provider_transaction_id is not None:
        provider_transaction_id = str(provider_transaction_id)

    digest = _payload_digest(payload)
    evidence = _normalized_evidence(
        payload=payload,
        server_key=server_key,
    )

    payment = Payment.objects.filter(
        merchant_reference=merchant_reference,
    ).first()

    event, _ = ProviderEvent.objects.get_or_create(
        provider="midtrans",
        provider_event_id=f"payload:{digest}",
        defaults={
            "payment": payment,
            "merchant_reference": merchant_reference,
            "provider_transaction_id": provider_transaction_id,
            "event_type": "transaction-status",
            "amount_minor": _amount_minor(
                payload.get("gross_amount")
            ),
            "currency": str(
                payload.get("currency") or "IDR"
            ),
            "payload_digest": digest,
            "authenticity_verified_at": timezone.now(),
            "authenticity_method": authenticity_method,
            **evidence,
        },
    )

    return event


def ingest_midtrans_notification(
    *,
    payload: dict,
    server_key: str,
) -> ProviderEvent:
    if not verify_notification_signature(
        payload=payload,
        server_key=server_key,
    ):
        raise MidtransNotificationAuthenticationError(
            "Midtrans notification signature verification failed."
        )

    return _persist_authenticated_midtrans_event(
        payload=payload,
        server_key=server_key,
        authenticity_method="midtrans-sha512",
    )


def _open_partial_chargeback_case(
    *,
    payment: Payment,
    provider_event: ProviderEvent,
) -> None:
    PaymentIntegrityCase.objects.get_or_create(
        case_key=f"PARTIAL_CHARGEBACK:event:{provider_event.pk}",
        defaults={
            "order_id": payment.order_id,
            "payment": payment,
            "provider_event": provider_event,
            "reason": (
                PaymentIntegrityCase.Reason.PARTIAL_CHARGEBACK
            ),
            "status": PaymentIntegrityCase.Status.OPEN,
        },
    )


def _upsert_cumulative_adjustment(
    *,
    payment: Payment,
    provider_event: ProviderEvent,
) -> None:
    if provider_event.is_partial_adjustment and (
        provider_event.adjustment_kind
        == FinancialAdjustment.Kind.CHARGEBACK
    ):
        _open_partial_chargeback_case(
            payment=payment,
            provider_event=provider_event,
        )
        return

    target = provider_event.adjustment_cumulative_amount_minor

    if target is None:
        if (
            provider_event.adjustment_kind
            == FinancialAdjustment.Kind.CHARGEBACK
            and not provider_event.is_partial_adjustment
        ):
            target = payment.amount_minor
        else:
            raise MidtransProtocolError(
                "Midtrans adjustment is missing cumulative amount."
            )

    recorded_before = (
        FinancialAdjustment.objects.filter(
            payment=payment,
            kind=provider_event.adjustment_kind,
        )
        .aggregate(total=Sum("amount_minor"))
        ["total"]
        or 0
    )

    reference = provider_event.provider_adjustment_reference

    if reference:
        existing = FinancialAdjustment.objects.filter(
            payment=payment,
            provider_reference=reference,
        ).first()
    else:
        existing = None

    if existing is not None:
        if (
            provider_event.adjustment_confirmed
            and existing.status
            == FinancialAdjustment.Status.PENDING
        ):
            confirm_financial_adjustment(
                adjustment=existing,
            )
        return

    delta = target - recorded_before

    if delta <= 0:
        return

    adjustment = FinancialAdjustment.objects.create(
        payment=payment,
        kind=provider_event.adjustment_kind,
        status=FinancialAdjustment.Status.PENDING,
        amount_minor=delta,
        currency=payment.currency,
        provider_reference=reference,
        initiation_reason=(
            "Observed from authenticated Midtrans transaction status."
        ),
    )

    if provider_event.adjustment_confirmed:
        confirm_financial_adjustment(
            adjustment=adjustment,
        )


def _record_reversal(
    *,
    payment: Payment,
    provider_event: ProviderEvent,
) -> None:
    reference = f"reversal:{provider_event.pk}"

    adjustment, _ = FinancialAdjustment.objects.get_or_create(
        payment=payment,
        provider_reference=reference,
        defaults={
            "kind": FinancialAdjustment.Kind.REVERSAL,
            "status": FinancialAdjustment.Status.PENDING,
            "amount_minor": payment.amount_minor,
            "currency": payment.currency,
            "initiation_reason": (
                "Midtrans deny observed after successful acquisition."
            ),
        },
    )

    if adjustment.status == FinancialAdjustment.Status.PENDING:
        confirm_financial_adjustment(
            adjustment=adjustment,
        )


@transaction.atomic
def process_midtrans_event(
    *,
    provider_event: ProviderEvent,
) -> None:
    locked_event = (
        ProviderEvent.objects
        .select_for_update()
        .get(pk=provider_event.pk)
    )

    if (
        locked_event.processing_status
        == ProviderEvent.ProcessingStatus.PROCESSED
    ):
        return

    if not locked_event.observed_payment_status:
        locked_event.processing_status = (
            ProviderEvent.ProcessingStatus.FAILED
        )
        locked_event.attempt_count += 1
        locked_event.last_error_code = (
            "MIDTRANS_UNSUPPORTED_TRANSACTION_STATUS"
        )
        locked_event.save(
            update_fields=[
                "processing_status",
                "attempt_count",
                "last_error_code",
            ]
        )
        return

    payment = locked_event.payment

    if payment is None:
        payment = Payment.objects.filter(
            merchant_reference=locked_event.merchant_reference,
        ).first()

    was_succeeded = bool(
        payment is not None
        and payment.status == Payment.Status.SUCCEEDED
    )

    process_provider_event(
        provider_event=locked_event,
        observed_payment_status=(
            locked_event.observed_payment_status
        ),
    )

    locked_event.refresh_from_db()

    mismatch_reasons = {
        PaymentIntegrityCase.Reason.AMOUNT_MISMATCH,
        PaymentIntegrityCase.Reason.CURRENCY_MISMATCH,
        PaymentIntegrityCase.Reason.PROVIDER_IDENTITY_MISMATCH,
    }

    if locked_event.integrity_cases.filter(
        reason__in=mismatch_reasons,
    ).exists():
        return

    if locked_event.payment_id is None:
        return

    payment = (
        Payment.objects
        .select_for_update()
        .get(pk=locked_event.payment_id)
    )

    if (
        locked_event.provider_status == "deny"
        and was_succeeded
    ):
        _record_reversal(
            payment=payment,
            provider_event=locked_event,
        )
        return

    if locked_event.adjustment_kind:
        _upsert_cumulative_adjustment(
            payment=payment,
            provider_event=locked_event,
        )


@transaction.atomic
def reconcile_midtrans_payment(
    *,
    payment: Payment,
    client: MidtransClient,
) -> ProviderEvent:
    locked_payment = (
        Payment.objects
        .select_for_update()
        .get(pk=payment.pk)
    )

    payload = client.get_transaction_status(
        merchant_reference=locked_payment.merchant_reference,
    )

    event = _persist_authenticated_midtrans_event(
        payload=payload,
        server_key=client.server_key,
        authenticity_method="midtrans-status-api",
    )

    process_midtrans_event(
        provider_event=event,
    )

    return event
