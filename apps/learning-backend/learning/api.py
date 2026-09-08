from django.db.models import Prefetch
from django.http import JsonResponse

from .models import Course, CourseRelease


def catalog(request):
    published_releases = (
        CourseRelease.objects
        .filter(is_published=True)
        .order_by("-release_number")
        .prefetch_related("modules__lessons")
    )

    courses = (
        Course.objects
        .filter(is_active=True)
        .order_by("title")
        .prefetch_related(
            Prefetch(
                "releases",
                queryset=published_releases,
                to_attr="published_releases",
            )
        )
    )

    payload = []

    for course in courses:
        if not course.published_releases:
            continue

        release = course.published_releases[0]
        modules = list(release.modules.all())

        lessons = [
            lesson
            for module in modules
            for lesson in module.lessons.all()
        ]

        payload.append(
            {
                "id": str(course.id),
                "subject": course.subject,
                "title": release.title,
                "summary": course.summary,
                "level": course.level,
                "moduleCount": len(modules),
                "lessonCount": len(lessons),
                "durationMinutes": sum(
                    lesson.duration_minutes
                    for lesson in lessons
                ),
                "href": f"/courses/{course.slug}",
            }
        )

    return JsonResponse({"courses": payload})


def course_detail(request, slug):
    try:
        course = (
            Course.objects
            .prefetch_related("releases__modules__lessons")
            .get(slug=slug, is_active=True)
        )
    except Course.DoesNotExist:
        return JsonResponse(
            {"detail": "Course not found."},
            status=404,
        )

    release = (
        course.releases
        .filter(is_published=True)
        .order_by("-release_number")
        .first()
    )

    if release is None:
        return JsonResponse(
            {"detail": "Published course release not found."},
            status=404,
        )

    modules = []

    for module in release.modules.all():
        modules.append(
            {
                "id": str(module.id),
                "title": module.title,
                "items": [
                    {
                        "id": str(lesson.id),
                        "kind": "lesson",
                        "title": lesson.title,
                        "durationMinutes": lesson.duration_minutes,
                    }
                    for lesson in module.lessons.all()
                ],
            }
        )

    return JsonResponse(
        {
            "release": {
                "id": str(release.id),
                "courseId": str(course.id),
                "release": release.release_number,
                "title": release.title,
                "modules": modules,
            },
            "kicker": course.subject,
            "summary": course.summary,
            "level": course.level,
            "outcomes": course.outcome_list,
            "audience": course.audience,
            "primaryAction": {
                "label": "Start course",
                "href": f"/learn/{course.slug}",
            },
        }
    )
