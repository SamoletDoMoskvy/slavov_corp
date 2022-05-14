from django.contrib import admin
from django.urls import path, include

from cargo.views import get_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cargo/get_report/<str:id>/", get_report)
]
