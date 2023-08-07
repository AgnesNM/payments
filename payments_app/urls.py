from django.urls import path

from . import views

app_name = "payments_app"

#/payments_app/validation

urlpatterns = [
    path("", views.celery_view, name="celery_view"),
    path("validation/", views.validation, name="validation"),
    path("confirmation/", views.confirmation, name="confirmation"),
]

