import uuid

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from learning.models import Course, CourseRelease, Enrollment

from .models import CourseEntitlement, CourseOffer, Order, Payment


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
