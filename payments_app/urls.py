from django.urls import path

from . import views

app_name = "payments_app"

urlpatterns = [
    path("", views.celery_view, name="celery_view")
]

