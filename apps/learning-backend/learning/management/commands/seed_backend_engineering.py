from django.core.management.base import BaseCommand
from django.db import transaction

from learning.models import Course, CourseRelease, Lesson, Module


class Command(BaseCommand):
    help = "Seed Backend Engineering Foundations."

    @transaction.atomic
    def handle(self, *args, **options):
        course, _ = Course.objects.update_or_create(
            slug="backend-engineering",
            defaults={
                "subject": "BACKEND ENGINEERING",
                "title": "Backend Engineering Foundations",
                "summary": (
                    "Learn how reliable backend systems actually behave—from "
                    "HTTP and API contracts to identity boundaries, sessions, "
                    "and production testing."
                ),
                "level": "Foundation",
                "audience": (
                    "Developers who want to move beyond framework recipes and "
                    "reason confidently about production backend systems."
                ),
                "outcomes": "\n".join(
                    [
                        "Model HTTP requests, responses, and trust boundaries clearly.",
                        "Design APIs around stable product contracts instead of database structure.",
                        "Separate authentication, authorization, sessions, and server authority.",
                        "Choose session mechanics from failure modes and revocation requirements.",
                        "Test observable contracts without coupling tests to implementation details.",
                    ]
                ),
                "is_active": True,
            },
        )

        release, _ = CourseRelease.objects.update_or_create(
            course=course,
            release_number=1,
            defaults={
                "title": "Backend Engineering Foundations",
                "is_published": True,
            },
        )

        release.modules.all().delete()

        curriculum = [
            (
                "Web & API Foundations",
                [
                    ("http", "How HTTP actually moves", 12),
                    ("resource-oriented-apis", "Designing resource-oriented APIs", 16),
                ],
            ),
            (
                "Trust Boundaries",
                [
                    ("authentication-authorization", "Authentication & authorization", 18),
                    ("sessions-tokens-revocation", "Sessions, tokens, and revocation", 15),
                ],
            ),
            (
                "Production Discipline",
                [
                    ("testing-contracts", "Testing contracts, not implementation", 20),
                ],
            ),
        ]

        lesson_count = 0

        for module_position, (module_title, lessons) in enumerate(curriculum, start=1):
            module = Module.objects.create(
                release=release,
                position=module_position,
                title=module_title,
            )

            for lesson_position, (slug, title, duration) in enumerate(
                lessons,
                start=1,
            ):
                Lesson.objects.create(
                    module=module,
                    position=lesson_position,
                    slug=slug,
                    eyebrow=(
                        f"MODULE {module_position:02d} · "
                        f"LESSON {lesson_position:02d}"
                    ),
                    title=title,
                    duration_minutes=duration,
                )
                lesson_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {course.title}: "
                f"{len(curriculum)} modules, {lesson_count} lessons."
            )
        )
