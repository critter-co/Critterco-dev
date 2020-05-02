from .models import Biz, Hours
from rest_framework import viewsets, permissions
from .serializers import BizSerializer, HoursSerializer

# Biz Viewset


class BizViewSet(viewsets.ModelViewSet):
    queryset = Biz.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BizSerializer


class HoursViewSet(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HoursSerializer
