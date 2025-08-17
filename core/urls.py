from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from leads.views import LeadViewSet
from django.db import connection
import os

router = DefaultRouter()
router.register(r"leads", LeadViewSet, basename="lead")

def health(_request):
    cfg = connection.settings_dict
    return JsonResponse({
        "status": "ok",
        "db_engine": cfg.get("ENGINE"),
        "db_name": cfg.get("NAME"),
        "has_DATABASE_URL": bool(os.getenv("DATABASE_URL")),
    })

urlpatterns = [
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
