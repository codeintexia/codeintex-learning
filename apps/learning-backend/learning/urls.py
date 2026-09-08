from django.urls import path

from .api import catalog, course_detail

urlpatterns = [
    path("catalog/", catalog, name="catalog"),
    path(
        "courses/<slug:slug>/",
        course_detail,
        name="course-detail",
    ),
]
