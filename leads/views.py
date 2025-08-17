from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.order_by("-created_at")
    serializer_class = LeadSerializer
