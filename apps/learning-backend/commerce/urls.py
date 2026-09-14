from django.urls import path

from .http_api import (
    course_checkout,
    midtrans_notification,
)


urlpatterns = [
    path(
        "courses/<slug:slug>/checkout/",
        course_checkout,
        name="course-checkout",
    ),
    path(
        "providers/midtrans/notifications/",
        midtrans_notification,
        name="midtrans-notification",
    ),
]
