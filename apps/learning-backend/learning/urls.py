from django.urls import path

from .api import catalog, course_detail, player_content

urlpatterns = [
    path("catalog/", catalog, name="catalog"),
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
]
