from django.core.management.base import BaseCommand
from django.db import transaction

from learning.models import Course, CourseRelease, Lesson, Module


COURSE_TITLE = "Backend Engineering Foundations"

SUMMARY = (
    "Learn how reliable backend systems actually behave—from "
    "HTTP and API contracts to identity boundaries, sessions, "
    "and production testing."
)

AUDIENCE = (
    "Developers who want to move beyond framework recipes and "
    "reason confidently about production backend systems."
)

OUTCOMES = "\n".join(
    [
        "Model HTTP requests, responses, and trust boundaries clearly.",
        "Design APIs around stable product contracts instead of database structure.",
        "Separate authentication, authorization, sessions, and server authority.",
        "Choose session mechanics from failure modes and revocation requirements.",
        "Test observable contracts without coupling tests to implementation details.",
    ]
)

CURRICULUM = [
    {
        "title": "Web & API Foundations",
        "lessons": [
            {
                "slug": "http",
                "title": "How HTTP actually moves",
                "duration": 12,
                "summary": (
                    "Build a concrete mental model for requests, responses, "
                    "intermediaries, and failure before designing an API."
                ),
                "sections": [
                    {
                        "heading": "Start with the boundary",
                        "body": (
                            "A browser does not call your database. It crosses "
                            "a sequence of trust and transport boundaries. Good "
                            "backend design begins by identifying those boundaries "
                            "explicitly."
                        ),
                        "code": "",
                    },
                    {
                        "heading": "Request as a contract",
                        "body": (
                            "Treat method, target, headers, and body as a contract "
                            "between independently evolving systems."
                        ),
                        "code": (
                            "GET /v1/courses/backend-engineering\n"
                            "Accept: application/json"
                        ),
                    },
                ],
            },
            {
                "slug": "resource-oriented-apis",
                "title": "Designing resource-oriented APIs",
                "duration": 16,
                "summary": (
                    "Turn product language into stable resources and operations "
                    "without leaking database structure."
                ),
                "sections": [
                    {
                        "heading": "Domain language first",
                        "body": (
                            "An API contract should speak in learner and product "
                            "concepts, not table names or framework internals."
                        ),
                        "code": "",
                    },
                ],
            },
        ],
    },
    {
        "title": "Trust Boundaries",
        "lessons": [
            {
                "slug": "authentication-authorization",
                "title": "Authentication & authorization",
                "duration": 18,
                "summary": (
                    "Separate identity from permission so security rules remain "
                    "clear as the platform grows."
                ),
                "sections": [
                    {
                        "heading": "Authentication answers one question",
                        "body": (
                            "Authentication establishes who is making the request. "
                            "It should not silently decide everything that identity "
                            "is allowed to do."
                        ),
                        "code": "",
                    },
                    {
                        "heading": "Authorization is contextual",
                        "body": (
                            "The same identity may be a learner in Learning, an "
                            "author in Research, and a client in Services. Each "
                            "product owns its authorization policy."
                        ),
                        "code": (
                            'identity = authenticate(request)\n'
                            'authorize(identity, action="course:learn", '
                            'resource=course)'
                        ),
                    },
                    {
                        "heading": "Make the server authoritative",
                        "body": (
                            "The browser can request a privileged action, but the "
                            "server validates identity, entitlement, ownership, "
                            "and policy before changing canonical state."
                        ),
                        "code": "",
                    },
                ],
            },
            {
                "slug": "sessions-tokens-revocation",
                "title": "Sessions, tokens, and revocation",
                "duration": 15,
                "summary": (
                    "Choose session mechanics based on trust boundaries rather "
                    "than framework fashion."
                ),
                "sections": [
                    {
                        "heading": "Start from failure modes",
                        "body": (
                            "Ask how credentials expire, how a compromised session "
                            "is revoked, and which system is authoritative before "
                            "choosing a token format."
                        ),
                        "code": "",
                    },
                ],
            },
        ],
    },
    {
        "title": "Production Discipline",
        "lessons": [
            {
                "slug": "testing-contracts",
                "title": "Testing contracts, not implementation",
                "duration": 20,
                "summary": (
                    "Protect behavior that matters to users and integrations "
                    "while keeping implementation replaceable."
                ),
                "sections": [
                    {
                        "heading": "Test the promise",
                        "body": (
                            "A durable test asserts observable behavior and domain "
                            "invariants, not every internal function call."
                        ),
                        "code": "",
                    },
                ],
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Bootstrap Backend Engineering Foundations."

    @transaction.atomic
    def handle(self, *args, **options):
        course, course_created = Course.objects.get_or_create(
            slug="backend-engineering",
            defaults={
                "subject": "BACKEND ENGINEERING",
                "title": COURSE_TITLE,
                # Temporary compatibility fields during expand-contract.
                "summary": SUMMARY,
                "level": "Foundation",
                "audience": AUDIENCE,
                "outcomes": OUTCOMES,
                "is_active": True,
            },
        )

        if not course_created:
            course.subject = "BACKEND ENGINEERING"
            course.title = COURSE_TITLE
            course.is_active = True
            course.save(
                update_fields=[
                    "subject",
                    "title",
                    "is_active",
                    "updated_at",
                ]
            )

        release, release_created = CourseRelease.objects.get_or_create(
            course=course,
            release_number=1,
            defaults={
                "title": COURSE_TITLE,
                "summary": SUMMARY,
                "level": "Foundation",
                "audience": AUDIENCE,
                "outcomes": OUTCOMES,
                "is_published": False,
            },
        )

        if not release_created and release.is_published:
            self.stdout.write(
                self.style.WARNING(
                    "Release 1 is already published; no mutation performed."
                )
            )
            return

        release.title = COURSE_TITLE
        release.summary = SUMMARY
        release.level = "Foundation"
        release.audience = AUDIENCE
        release.outcomes = OUTCOMES
        release.is_published = False
        release.save()

        release.modules.all().delete()

        lesson_count = 0

        for module_position, module_data in enumerate(
            CURRICULUM,
            start=1,
        ):
            module = Module.objects.create(
                release=release,
                position=module_position,
                title=module_data["title"],
            )

            for lesson_position, lesson_data in enumerate(
                module_data["lessons"],
                start=1,
            ):
                Lesson.objects.create(
                    module=module,
                    position=lesson_position,
                    slug=lesson_data["slug"],
                    eyebrow=(
                        f"MODULE {module_position:02d} · "
                        f"LESSON {lesson_position:02d}"
                    ),
                    title=lesson_data["title"],
                    summary=lesson_data["summary"],
                    duration_minutes=lesson_data["duration"],
                    sections=[
                        ("section", section)
                        for section in lesson_data["sections"]
                    ],
                )

                lesson_count += 1

        release.is_published = True
        release.save(
            update_fields=[
                "is_published",
                "updated_at",
            ]
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {release.title}: "
                f"{len(CURRICULUM)} modules, "
                f"{lesson_count} lessons, "
                f"release {release.release_number} published."
            )
        )
