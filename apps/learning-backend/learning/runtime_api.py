from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from .models import (
    Course,
    Enrollment,
    Lesson,
    LessonProgress,
)


def _authentication_required(request):
    if request.user.is_authenticated:
        return None

    return JsonResponse(
        {"detail": "Authentication required."},
        status=401,
    )


def _course(slug):
    return (
        Course.objects
        .filter(
            slug=slug,
            is_active=True,
        )
        .first()
    )


def _latest_published_release(course):
    return (
        course.releases
        .filter(is_published=True)
        .order_by("-release_number")
        .first()
    )


def _learner_enrollment_for_course(learner, course):
    return (
        Enrollment.objects
        .select_related("course_release")
        .filter(
            learner=learner,
            course_release__course=course,
        )
        .order_by(
            "-enrolled_at",
            "-course_release__release_number",
        )
        .first()
    )


def _progress_payload(enrollment):
    lessons = list(
        Lesson.objects
        .filter(
            module__release=enrollment.course_release,
        )
        .order_by(
            "module__position",
            "position",
        )
    )

    completed_ids = set(
        enrollment.lesson_progress.values_list(
            "lesson_id",
            flat=True,
        )
    )

    completed_item_ids = [
        str(lesson.id)
        for lesson in lessons
        if lesson.id in completed_ids
    ]

    first_incomplete = next(
        (
            lesson
            for lesson in lessons
            if lesson.id not in completed_ids
        ),
        None,
    )

    if first_incomplete is not None:
        current_item_id = str(first_incomplete.id)
    elif lessons:
        current_item_id = str(lessons[-1].id)
    else:
        current_item_id = None

    total_items = len(lessons)
    completed_items = len(completed_item_ids)

    progress_percent = (
        round((completed_items / total_items) * 100)
        if total_items
        else 0
    )

    return {
        "enrollmentId": str(enrollment.id),
        "releaseId": str(enrollment.course_release_id),
        "release": enrollment.course_release.release_number,
        "completedItemIds": completed_item_ids,
        "completedItems": completed_items,
        "totalItems": total_items,
        "progressPercent": progress_percent,
        "currentItemId": current_item_id,
    }


@require_POST
def course_enrollment(request, slug):
    authentication_error = _authentication_required(request)

    if authentication_error is not None:
        return authentication_error

    course = _course(slug)

    if course is None:
        return JsonResponse(
            {"detail": "Course not found."},
            status=404,
        )

    release = _latest_published_release(course)

    if release is None:
        return JsonResponse(
            {"detail": "Published course release not found."},
            status=404,
        )

    enrollment, created = Enrollment.objects.get_or_create(
        learner=request.user,
        course_release=release,
    )

    return JsonResponse(
        {
            "created": created,
            "progress": _progress_payload(enrollment),
        },
        status=201 if created else 200,
    )


@require_GET
def course_progress(request, slug):
    authentication_error = _authentication_required(request)

    if authentication_error is not None:
        return authentication_error

    course = _course(slug)

    if course is None:
        return JsonResponse(
            {"detail": "Course not found."},
            status=404,
        )

    enrollment = _learner_enrollment_for_course(
        request.user,
        course,
    )

    if enrollment is None:
        return JsonResponse(
            {"detail": "Enrollment not found."},
            status=404,
        )

    return JsonResponse(
        {
            "progress": _progress_payload(enrollment),
        }
    )


@require_POST
def complete_lesson(request, slug, lesson_id):
    authentication_error = _authentication_required(request)

    if authentication_error is not None:
        return authentication_error

    course = _course(slug)

    if course is None:
        return JsonResponse(
            {"detail": "Course not found."},
            status=404,
        )

    enrollment = _learner_enrollment_for_course(
        request.user,
        course,
    )

    if enrollment is None:
        return JsonResponse(
            {"detail": "Enrollment not found."},
            status=404,
        )

    lesson = (
        Lesson.objects
        .filter(
            pk=lesson_id,
            module__release=enrollment.course_release,
        )
        .first()
    )

    if lesson is None:
        return JsonResponse(
            {"detail": "Lesson not found in enrolled release."},
            status=404,
        )

    _, created = LessonProgress.objects.get_or_create(
        enrollment=enrollment,
        lesson=lesson,
    )

    return JsonResponse(
        {
            "created": created,
            "progress": _progress_payload(enrollment),
        },
        status=201 if created else 200,
    )
