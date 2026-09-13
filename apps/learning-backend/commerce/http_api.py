import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from commerce.providers.midtrans_workflows import (
    MidtransNotificationAuthenticationError,
    ingest_midtrans_notification,
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
