from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from learning.models import Course

from .models import CourseEntitlement, CourseOffer, Order


class CommerceServiceError(Exception):
    """Base exception for expected Commerce service rejections."""


class OpenOrderExistsError(CommerceServiceError):
    """Raised when a non-expired OPEN Order already exists."""


class ActivePurchaseEntitlementError(CommerceServiceError):
    """Raised when the learner already has active purchased access."""


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
