import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from commerce.models import CourseEntitlement
from learning.models import Course, Enrollment


E2E_USERNAME = "codeintex-e2e"
FIXTURE_FLAG_ENV = "CODEINTEX_E2E_FIXTURES"
PASSWORD_ENV = "CODEINTEX_E2E_PASSWORD"


class Command(BaseCommand):
    help = (
        "Prepare the dedicated Playwright learner fixture without "
        "creating fake commercial transactions."
    )

    @transaction.atomic
    def handle(self, *args, **options):
        if os.environ.get(FIXTURE_FLAG_ENV) != "1":
            raise CommandError(
                f"{FIXTURE_FLAG_ENV}=1 is required."
            )

        password = os.environ.get(PASSWORD_ENV)

        if not password:
            raise CommandError(
                f"{PASSWORD_ENV} is required."
            )

        course = (
            Course.objects
            .filter(
                slug="backend-engineering",
                is_active=True,
            )
            .first()
        )

        if course is None:
            raise CommandError(
                "backend-engineering course is missing. "
                "Run seed_backend_engineering first."
            )

        release = (
            course.releases
            .filter(is_published=True)
            .order_by("-release_number")
            .first()
        )

        if release is None:
            raise CommandError(
                "backend-engineering has no published release."
            )

        User = get_user_model()

        learner, _ = User.objects.get_or_create(
            username=E2E_USERNAME,
        )

        learner.set_password(password)

        if hasattr(learner, "is_active"):
            learner.is_active = True
            learner.save(
                update_fields=[
                    "password",
                    "is_active",
                ]
            )
        else:
            learner.save(
                update_fields=["password"]
            )

        CourseEntitlement.objects.get_or_create(
            learner=learner,
            course=course,
            source=CourseEntitlement.Source.ADMIN_GRANT,
            status=CourseEntitlement.Status.ACTIVE,
            defaults={
                "grant_reason": (
                    "Dedicated Playwright E2E learner fixture."
                ),
            },
        )

        # This account exists only for deterministic E2E verification.
        # Recreate its enrollment so each run starts with zero progress
        # and is pinned to the current published release.
        Enrollment.objects.filter(
            learner=learner,
            course_release__course=course,
        ).delete()

        enrollment = Enrollment.objects.create(
            learner=learner,
            course_release=release,
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Prepared Playwright learner "
                f"{E2E_USERNAME} on "
                f"backend-engineering release "
                f"{release.release_number}; "
                f"enrollment={enrollment.pk}"
            )
        )
