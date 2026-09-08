import os

from django.core.exceptions import ImproperlyConfigured

from .base import *


def required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()

    if not value:
        raise ImproperlyConfigured(
            f"Required environment variable {name} is not set."
        )

    return value


def required_hosts(name: str) -> list[str]:
    hosts = [
        host.strip()
        for host in required_env(name).split(",")
        if host.strip()
    ]

    if not hosts or "*" in hosts:
        raise ImproperlyConfigured(
            f"{name} must contain explicit hostnames and must not contain '*'."
        )

    return hosts


DEBUG = False

SECRET_KEY = required_env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = required_hosts("DJANGO_ALLOWED_HOSTS")

WAGTAILADMIN_BASE_URL = required_env(
    "WAGTAILADMIN_BASE_URL"
).rstrip("/")

if not WAGTAILADMIN_BASE_URL.startswith("https://"):
    raise ImproperlyConfigured(
        "WAGTAILADMIN_BASE_URL must use https:// in production."
    )

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": required_env("DJANGO_DB_NAME"),
        "USER": required_env("DJANGO_DB_USER"),
        "PASSWORD": required_env("DJANGO_DB_PASSWORD"),
        "HOST": required_env("DJANGO_DB_HOST"),
        "PORT": os.environ.get("DJANGO_DB_PORT", "5432"),
        "OPTIONS": {
            "sslmode": os.environ.get(
                "DJANGO_DB_SSLMODE",
                "require",
            ),
        },
    }
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

STORAGES["staticfiles"]["BACKEND"] = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)
