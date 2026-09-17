from django.urls import path

from .http_api import (
    course_checkout,
    course_offer,
    midtrans_notification,
)


urlpatterns = [
    path(
        "courses/<slug:slug>/offer/",
        course_offer,
        name="course-offer",
    ),
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
