from django.urls import path

from .http_api import midtrans_notification


urlpatterns = [
    path(
        "providers/midtrans/notifications/",
        midtrans_notification,
        name="midtrans-notification",
    ),
]
