from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from leads.views import LeadViewSet

router = DefaultRouter()
router.register(r"leads", LeadViewSet, basename="lead")

def health(_request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # your API stays under /api/
]
