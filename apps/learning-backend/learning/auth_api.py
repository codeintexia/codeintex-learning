import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST


def _json_body(request):
    try:
        return json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        return None


@require_GET
@ensure_csrf_cookie
def csrf(request):
    return JsonResponse(
        {
            "csrfToken": get_token(request),
        }
    )


@require_GET
def session(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "authenticated": False,
                "user": None,
            }
        )

    return JsonResponse(
        {
            "authenticated": True,
            "user": {
                "id": str(request.user.pk),
                "username": request.user.get_username(),
            },
        }
    )


@require_POST
def log_in(request):
    payload = _json_body(request)

    if payload is None:
        return JsonResponse(
            {"detail": "Invalid JSON body."},
            status=400,
        )

    username = payload.get("username")
    password = payload.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return JsonResponse(
            {"detail": "Username and password are required."},
            status=400,
        )

    user = authenticate(
        request,
        username=username,
        password=password,
    )

    if user is None:
        return JsonResponse(
            {"detail": "Invalid credentials."},
            status=401,
        )

    login(request, user)

    return JsonResponse(
        {
            "authenticated": True,
            "user": {
                "id": str(user.pk),
                "username": user.get_username(),
            },
            "csrfToken": get_token(request),
        }
    )


@require_POST
def log_out(request):
    logout(request)

    return JsonResponse(
        {
            "authenticated": False,
            "user": None,
            "csrfToken": get_token(request),
        }
    )
