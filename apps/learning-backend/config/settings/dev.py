import os

from .base import *

DEBUG = True

# Development-only key. Never use this value outside local development.
SECRET_KEY = "codeintex-learning-local-development-only-not-secret"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
]

WAGTAILADMIN_BASE_URL = "http://127.0.0.1:8000"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS = [
    "http" + "://" + "localhost:3000",
    "http" + "://" + "127.0.0.1:3000",
]

CSRF_TRUSTED_ORIGINS.extend(
    origin.strip()
    for origin in os.environ.get(
        "CODEINTEX_DEV_CSRF_TRUSTED_ORIGINS",
        "",
    ).split(",")
    if origin.strip()
)
