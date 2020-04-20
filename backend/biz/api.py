from .models import Biz
from rest_framework import viewsets, permissions
from .serializers import BizSerializer

# Biz Viewset


class BizViewSet(viewsets.ModelViewSet):
    queryset = Biz.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BizSerializer
