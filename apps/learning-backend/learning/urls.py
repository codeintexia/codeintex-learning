from django.urls import path

from .api import (
    catalog,
    course_detail,
    player_content,
)
from .auth_api import (
    csrf,
    log_in,
    log_out,
    session,
)
from .runtime_api import (
    complete_lesson,
    course_enrollment,
    course_progress,
)

urlpatterns = [
    path(
        "auth/csrf/",
        csrf,
        name="auth-csrf",
    ),
    path(
        "auth/session/",
        session,
        name="auth-session",
    ),
    path(
        "auth/login/",
        log_in,
        name="auth-login",
    ),
    path(
        "auth/logout/",
        log_out,
        name="auth-logout",
    ),
    path(
        "catalog/",
        catalog,
        name="catalog",
    ),
    path(
        "courses/<slug:slug>/",
        course_detail,
        name="course-detail",
    ),
    path(
        "courses/<slug:slug>/player/",
        player_content,
        name="player-content",
    ),
    path(
        "courses/<slug:slug>/enrollment/",
        course_enrollment,
        name="course-enrollment",
    ),
    path(
        "courses/<slug:slug>/progress/",
        course_progress,
        name="course-progress",
    ),
    path(
        "courses/<slug:slug>/lessons/<uuid:lesson_id>/complete/",
        complete_lesson,
        name="complete-lesson",
    ),
]
