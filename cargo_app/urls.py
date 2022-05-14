from django.urls import path

from .views import get_report


urlpatterns = [
    path("cargo/get_report/<str:id>/", get_report)
]
