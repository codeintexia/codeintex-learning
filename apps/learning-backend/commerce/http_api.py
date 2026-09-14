import json
from datetime import timedelta

import requests
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from learning.models import Course

from commerce.models import (
    CourseEntitlement,
    CourseOffer,
    Order,
    Payment,
)
from commerce.providers.midtrans import (
    MidtransClient,
    MidtransError,
)
from commerce.providers.midtrans_workflows import (
    MidtransNotificationAuthenticationError,
    ingest_midtrans_notification,
)
from commerce.services import (
    ActivePurchaseEntitlementError,
    OpenOrderExistsError,
    OrderNotPayableError,
    PayablePaymentExistsError,
    SuccessfulPaymentExistsError,
    create_order,
    create_payment,
)


CHECKOUT_LIFETIME = timedelta(hours=24)


def _checkout_payload(*, order, payment):
    return {
        "checkout": {
            "orderId": str(order.pk),
            "paymentId": str(payment.pk),
            "redirectUrl": payment.checkout_url,
            "amountMinor": payment.amount_minor,
            "currency": payment.currency,
            "expiresAt": order.expires_at.isoformat(),
        }
    }


@require_POST
def course_checkout(request, slug):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"detail": "Authentication required."},
            status=401,
        )

    server_key = getattr(
        settings,
        "MIDTRANS_SERVER_KEY",
        "",
    ).strip()

    if not server_key:
        return JsonResponse(
            {"error": "payment_provider_unavailable"},
            status=503,
        )

    course = (
        Course.objects
        .filter(
            slug=slug,
            is_active=True,
        )
        .first()
    )

    if course is None:
        return JsonResponse(
            {"detail": "Course not found."},
            status=404,
        )

    if not course.releases.filter(is_published=True).exists():
        return JsonResponse(
            {"error": "course_unavailable"},
            status=409,
        )

    if CourseEntitlement.objects.filter(
        learner=request.user,
        course=course,
        source=CourseEntitlement.Source.PURCHASE,
        status=CourseEntitlement.Status.ACTIVE,
    ).exists():
        return JsonResponse(
            {"error": "already_entitled"},
            status=409,
        )

    now = timezone.now()

    order = (
        Order.objects
        .select_related("offer")
        .filter(
            learner=request.user,
            course=course,
            status=Order.Status.OPEN,
            expires_at__gt=now,
        )
        .order_by("-created_at")
        .first()
    )

    created_order = False

    if order is None:
        offer = (
            CourseOffer.objects
            .filter(
                course=course,
                currency="IDR",
                is_active=True,
            )
            .first()
        )

        if offer is None:
            return JsonResponse(
                {"error": "offer_unavailable"},
                status=409,
            )

        try:
            order = create_order(
                learner=request.user,
                course=course,
                offer_id=offer.pk,
                expires_at=now + CHECKOUT_LIFETIME,
            )
            created_order = True
        except ActivePurchaseEntitlementError:
            return JsonResponse(
                {"error": "already_entitled"},
                status=409,
            )
        except OpenOrderExistsError:
            order = (
                Order.objects
                .select_related("offer")
                .filter(
                    learner=request.user,
                    course=course,
                    status=Order.Status.OPEN,
                    expires_at__gt=timezone.now(),
                )
                .order_by("-created_at")
                .first()
            )

            if order is None:
                return JsonResponse(
                    {"error": "checkout_conflict"},
                    status=409,
                )

    payment = (
        Payment.objects
        .filter(
            order=order,
            status__in=[
                Payment.Status.CREATED,
                Payment.Status.PENDING,
            ],
        )
        .order_by("-created_at")
        .first()
    )

    created_payment = False

    if payment is not None and payment.provider != "midtrans":
        return JsonResponse(
            {"error": "payment_in_progress"},
            status=409,
        )

    if payment is None:
        try:
            payment = create_payment(
                order=order,
                provider="midtrans",
            )
            created_payment = True
        except PayablePaymentExistsError:
            payment = (
                Payment.objects
                .filter(
                    order=order,
                    status__in=[
                        Payment.Status.CREATED,
                        Payment.Status.PENDING,
                    ],
                )
                .order_by("-created_at")
                .first()
            )

            if payment is None:
                return JsonResponse(
                    {"error": "checkout_conflict"},
                    status=409,
                )

            if payment.provider != "midtrans":
                return JsonResponse(
                    {"error": "payment_in_progress"},
                    status=409,
                )
        except SuccessfulPaymentExistsError:
            return JsonResponse(
                {"error": "payment_already_succeeded"},
                status=409,
            )
        except OrderNotPayableError:
            return JsonResponse(
                {"error": "order_not_payable"},
                status=409,
            )

    if payment.checkout_url:
        return JsonResponse(
            _checkout_payload(
                order=order,
                payment=payment,
            ),
            status=200,
        )

    environment = getattr(
        settings,
        "MIDTRANS_ENVIRONMENT",
        "sandbox",
    ).strip() or "sandbox"

    client = MidtransClient(
        server_key=server_key,
        environment=environment,
    )

    try:
        checkout = client.create_snap_checkout(
            merchant_reference=payment.merchant_reference,
            amount_minor=payment.amount_minor,
            currency=payment.currency,
            idempotency_key=str(payment.operation_key),
        )
    except (MidtransError, requests.RequestException):
        return JsonResponse(
            {"error": "payment_provider_error"},
            status=502,
        )

    Payment.objects.filter(
        pk=payment.pk,
        checkout_url="",
    ).update(
        checkout_url=checkout.redirect_url,
    )

    payment.refresh_from_db()

    return JsonResponse(
        _checkout_payload(
            order=order,
            payment=payment,
        ),
        status=201 if created_order or created_payment else 200,
    )


@csrf_exempt
@require_POST
def midtrans_notification(request):
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "invalid_json"},
            status=400,
        )

    if not isinstance(payload, dict):
        return JsonResponse(
            {"error": "invalid_payload"},
            status=400,
        )

    server_key = getattr(
        settings,
        "MIDTRANS_SERVER_KEY",
        "",
    ).strip()

    if not server_key:
        return JsonResponse(
            {"error": "payment_provider_unavailable"},
            status=503,
        )

    try:
        ingest_midtrans_notification(
            payload=payload,
            server_key=server_key,
        )
    except MidtransNotificationAuthenticationError:
        return JsonResponse(
            {"error": "invalid_signature"},
            status=401,
        )

    return JsonResponse(
        {"status": "received"},
        status=200,
    )
