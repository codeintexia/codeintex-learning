import uuid

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from learning.models import Course, CourseRelease, Enrollment

from .models import CourseEntitlement, CourseOffer, Order, Payment
from .models import PaymentIntegrityCase, ProviderEvent


class CommerceServiceError(Exception):
    """Base exception for expected Commerce service rejections."""


class OpenOrderExistsError(CommerceServiceError):
    """Raised when a non-expired OPEN Order already exists."""


class ActivePurchaseEntitlementError(CommerceServiceError):
    """Raised when the learner already has active purchased access."""


class OrderNotPayableError(CommerceServiceError):
    """Raised when an Order is not OPEN and payable."""


class SuccessfulPaymentExistsError(CommerceServiceError):
    """Raised when the Order already has a successful Payment."""


class PayablePaymentExistsError(CommerceServiceError):
    """Raised when the Order already has a CREATED/PENDING Payment."""


class PaymentNotSuccessfulError(CommerceServiceError):
    """Raised when fulfillment is attempted before Payment succeeds."""


class OrderNotFulfillableError(CommerceServiceError):
    """Raised when the Order cannot be fulfilled."""


class PublishedCourseReleaseRequiredError(CommerceServiceError):
    """Raised when no published CourseRelease is available."""


@transaction.atomic
def create_order(
    *,
    learner,
    course: Course,
    offer_id,
    expires_at,
) -> Order:
    locked_learner = (
        get_user_model()
        .objects
        .select_for_update()
        .get(pk=learner.pk)
    )

    now = timezone.now()

    existing_open_order = (
        Order.objects
        .select_for_update()
        .filter(
            learner=locked_learner,
            course=course,
            status=Order.Status.OPEN,
        )
        .first()
    )

    if (
        existing_open_order is not None
        and existing_open_order.expires_at <= now
    ):
        existing_open_order.status = Order.Status.EXPIRED
        existing_open_order.save(update_fields=["status"])
        existing_open_order = None

    has_active_purchase_entitlement = (
        CourseEntitlement.objects.filter(
            learner=locked_learner,
            course=course,
            source=CourseEntitlement.Source.PURCHASE,
            status=CourseEntitlement.Status.ACTIVE,
        ).exists()
    )

    if has_active_purchase_entitlement:
        raise ActivePurchaseEntitlementError(
            "Learner already has an active purchase entitlement "
            "for this course."
        )

    if existing_open_order is not None:
        raise OpenOrderExistsError(
            "A live OPEN Order already exists for this learner "
            "and course."
        )

    offer = (
        CourseOffer.objects
        .select_for_update()
        .get(
            pk=offer_id,
            course=course,
            is_active=True,
        )
    )

    return Order.objects.create(
        learner=locked_learner,
        course=course,
        offer=offer,
        status=Order.Status.OPEN,
        subtotal_amount_minor=offer.amount_minor,
        discount_amount_minor=0,
        total_amount_minor=offer.amount_minor,
        currency=offer.currency,
        course_title_snapshot=course.title,
        expires_at=expires_at,
    )


@transaction.atomic
def create_payment(
    *,
    order: Order,
    provider: str,
) -> Payment:
    locked_order = (
        Order.objects
        .select_for_update()
        .get(pk=order.pk)
    )

    if locked_order.status != Order.Status.OPEN:
        raise OrderNotPayableError(
            "Payment can only be created for an OPEN Order."
        )

    if Payment.objects.filter(
        order=locked_order,
        status=Payment.Status.SUCCEEDED,
    ).exists():
        raise SuccessfulPaymentExistsError(
            "A successful Payment already exists for this Order."
        )

    if Payment.objects.filter(
        order=locked_order,
        status__in=[
            Payment.Status.CREATED,
            Payment.Status.PENDING,
        ],
    ).exists():
        raise PayablePaymentExistsError(
            "A payable Payment already exists for this Order."
        )

    return Payment.objects.create(
        order=locked_order,
        provider=provider,
        status=Payment.Status.CREATED,
        operation_key=uuid.uuid4(),
        merchant_reference=f"payment-{uuid.uuid4()}",
        amount_minor=locked_order.total_amount_minor,
        currency=locked_order.currency,
    )


@transaction.atomic
def fulfill_purchase(
    *,
    payment: Payment,
) -> None:
    locked_payment = (
        Payment.objects
        .select_for_update()
        .get(pk=payment.pk)
    )

    if locked_payment.status != Payment.Status.SUCCEEDED:
        raise PaymentNotSuccessfulError(
            "Purchase fulfillment requires a SUCCEEDED Payment."
        )

    locked_order = (
        Order.objects
        .select_for_update()
        .get(pk=locked_payment.order_id)
    )

    if locked_order.status == Order.Status.FULFILLED:
        return

    if locked_order.status != Order.Status.OPEN:
        raise OrderNotFulfillableError(
            "Only an OPEN Order can be fulfilled."
        )

    locked_learner = (
        get_user_model()
        .objects
        .select_for_update()
        .get(pk=locked_order.learner_id)
    )

    course_release = (
        CourseRelease.objects
        .filter(
            course_id=locked_order.course_id,
            is_published=True,
        )
        .order_by("-release_number")
        .first()
    )

    if course_release is None:
        raise PublishedCourseReleaseRequiredError(
            "Purchase fulfillment requires a published CourseRelease."
        )

    CourseEntitlement.objects.get_or_create(
        order=locked_order,
        defaults={
            "learner": locked_learner,
            "course_id": locked_order.course_id,
            "source": CourseEntitlement.Source.PURCHASE,
            "status": CourseEntitlement.Status.ACTIVE,
            "grant_reason": "Purchase fulfillment",
        },
    )

    Enrollment.objects.get_or_create(
        learner=locked_learner,
        course_release=course_release,
    )

    locked_order.status = Order.Status.FULFILLED
    locked_order.fulfilled_at = timezone.now()
    locked_order.save(
        update_fields=[
            "status",
            "fulfilled_at",
        ]
    )


def _integrity_case_key(
    *,
    reason: str,
    payment: Payment | None = None,
    provider_event: ProviderEvent | None = None,
) -> str:
    if provider_event is not None:
        identity = f"event:{provider_event.pk}"
    elif payment is not None:
        identity = f"payment:{payment.pk}"
    else:
        raise ValueError(
            "Integrity case requires a Payment or ProviderEvent."
        )

    return f"{reason}:{identity}"


def _open_payment_integrity_case(
    *,
    reason: str,
    payment: Payment | None = None,
    provider_event: ProviderEvent | None = None,
    order: Order | None = None,
) -> PaymentIntegrityCase:
    case, _ = PaymentIntegrityCase.objects.get_or_create(
        case_key=_integrity_case_key(
            reason=reason,
            payment=payment,
            provider_event=provider_event,
        ),
        defaults={
            "reason": reason,
            "status": PaymentIntegrityCase.Status.OPEN,
            "payment": payment,
            "provider_event": provider_event,
            "order": order,
        },
    )
    return case


def _next_payment_status(
    *,
    current_status: str,
    observed_status: str,
) -> str:
    valid_statuses = set(Payment.Status.values)

    if observed_status not in valid_statuses:
        raise CommerceServiceError(
            f"Unsupported observed Payment status: {observed_status}"
        )

    if current_status == Payment.Status.SUCCEEDED:
        return Payment.Status.SUCCEEDED

    if observed_status == Payment.Status.SUCCEEDED:
        return Payment.Status.SUCCEEDED

    terminal_non_success = {
        Payment.Status.FAILED,
        Payment.Status.CANCELLED,
        Payment.Status.EXPIRED,
    }

    if current_status in terminal_non_success:
        return current_status

    if (
        current_status == Payment.Status.PENDING
        and observed_status == Payment.Status.CREATED
    ):
        return Payment.Status.PENDING

    return observed_status


@transaction.atomic
def apply_payment_observation(
    *,
    payment: Payment,
    observed_status: str,
    provider_transaction_id: str | None = None,
    provider_event: ProviderEvent | None = None,
) -> Payment:
    locked_payment = (
        Payment.objects
        .select_for_update()
        .get(pk=payment.pk)
    )

    locked_order = (
        Order.objects
        .select_for_update()
        .get(pk=locked_payment.order_id)
    )

    if (
        provider_transaction_id
        and locked_payment.provider_transaction_id
        and (
            locked_payment.provider_transaction_id
            != provider_transaction_id
        )
    ):
        _open_payment_integrity_case(
            reason=(
                PaymentIntegrityCase.Reason
                .PROVIDER_IDENTITY_MISMATCH
            ),
            payment=locked_payment,
            provider_event=provider_event,
            order=locked_order,
        )
        return locked_payment

    update_fields = []

    if (
        provider_transaction_id
        and not locked_payment.provider_transaction_id
    ):
        locked_payment.provider_transaction_id = (
            provider_transaction_id
        )
        update_fields.append("provider_transaction_id")

    next_status = _next_payment_status(
        current_status=locked_payment.status,
        observed_status=observed_status,
    )

    if next_status != locked_payment.status:
        locked_payment.status = next_status
        update_fields.append("status")

    if (
        next_status == Payment.Status.SUCCEEDED
        and locked_payment.succeeded_at is None
    ):
        locked_payment.succeeded_at = timezone.now()
        update_fields.append("succeeded_at")

    if update_fields:
        locked_payment.save(update_fields=update_fields)

    if locked_payment.status != Payment.Status.SUCCEEDED:
        return locked_payment

    has_other_success = (
        Payment.objects
        .filter(
            order=locked_order,
            status=Payment.Status.SUCCEEDED,
        )
        .exclude(pk=locked_payment.pk)
        .exists()
    )

    if has_other_success:
        _open_payment_integrity_case(
            reason=(
                PaymentIntegrityCase.Reason
                .MULTIPLE_SUCCESSFUL_PAYMENTS
            ),
            payment=locked_payment,
            provider_event=provider_event,
            order=locked_order,
        )

    if locked_order.status in {
        Order.Status.CANCELLED,
        Order.Status.EXPIRED,
    }:
        _open_payment_integrity_case(
            reason=(
                PaymentIntegrityCase.Reason
                .LATE_PAYMENT_CLOSED_ORDER
            ),
            payment=locked_payment,
            provider_event=provider_event,
            order=locked_order,
        )
        return locked_payment

    if locked_order.status == Order.Status.OPEN:
        fulfill_purchase(payment=locked_payment)

    return locked_payment


def _mark_provider_event_processed(
    provider_event: ProviderEvent,
) -> None:
    provider_event.processing_status = (
        ProviderEvent.ProcessingStatus.PROCESSED
    )
    provider_event.processed_at = timezone.now()
    provider_event.last_error_code = None
    provider_event.save(
        update_fields=[
            "processing_status",
            "processed_at",
            "last_error_code",
        ]
    )


@transaction.atomic
def process_provider_event(
    *,
    provider_event: ProviderEvent,
    observed_payment_status: str,
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

    locked_event.processing_status = (
        ProviderEvent.ProcessingStatus.PROCESSING
    )
    locked_event.attempt_count += 1
    locked_event.save(
        update_fields=[
            "processing_status",
            "attempt_count",
        ]
    )

    if locked_event.payment_id:
        payment = (
            Payment.objects
            .select_for_update()
            .get(pk=locked_event.payment_id)
        )
    else:
        payment = (
            Payment.objects
            .select_for_update()
            .filter(
                merchant_reference=(
                    locked_event.merchant_reference
                )
            )
            .first()
        )

        if payment is not None:
            locked_event.payment = payment
            locked_event.save(update_fields=["payment"])

    if payment is None:
        _open_payment_integrity_case(
            reason=(
                PaymentIntegrityCase.Reason
                .PROVIDER_IDENTITY_MISMATCH
            ),
            provider_event=locked_event,
        )
        _mark_provider_event_processed(locked_event)
        return

    order = (
        Order.objects
        .select_for_update()
        .get(pk=payment.order_id)
    )

    identity_mismatch = (
        locked_event.provider != payment.provider
        or (
            locked_event.merchant_reference
            != payment.merchant_reference
        )
        or (
            locked_event.provider_transaction_id
            and payment.provider_transaction_id
            and (
                locked_event.provider_transaction_id
                != payment.provider_transaction_id
            )
        )
    )

    has_mismatch = False

    if identity_mismatch:
        _open_payment_integrity_case(
            reason=(
                PaymentIntegrityCase.Reason
                .PROVIDER_IDENTITY_MISMATCH
            ),
            payment=payment,
            provider_event=locked_event,
            order=order,
        )
        has_mismatch = True

    if (
        locked_event.amount_minor is not None
        and locked_event.amount_minor != payment.amount_minor
    ):
        _open_payment_integrity_case(
            reason=PaymentIntegrityCase.Reason.AMOUNT_MISMATCH,
            payment=payment,
            provider_event=locked_event,
            order=order,
        )
        has_mismatch = True

    if (
        locked_event.currency is not None
        and locked_event.currency != payment.currency
    ):
        _open_payment_integrity_case(
            reason=(
                PaymentIntegrityCase.Reason
                .CURRENCY_MISMATCH
            ),
            payment=payment,
            provider_event=locked_event,
            order=order,
        )
        has_mismatch = True

    if has_mismatch:
        _mark_provider_event_processed(locked_event)
        return

    apply_payment_observation(
        payment=payment,
        observed_status=observed_payment_status,
        provider_transaction_id=(
            locked_event.provider_transaction_id
        ),
        provider_event=locked_event,
    )

    _mark_provider_event_processed(locked_event)
