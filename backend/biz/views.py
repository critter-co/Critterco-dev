from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, permissions, authentication, serializers
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_gis.filters import DistanceToPointFilter
from .models import Biz, Hours
from .permissions import HasGroupPermission
from .serializers import BizSerializer, HoursSerializer

# Biz serializer views.
class BizViewSet(viewsets.ModelViewSet):
    queryset = Biz.objects.all()
    distance_filter_field = "location"
    distance_filter_convert_meters = True
    filter_backends = (DistanceToPointFilter,)
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [HasGroupPermission]
    required_groups = {
        "list": ["__all__"],
        "create": ["member", "biz_post"],
        "upate": ["member", "biz_edit"],
        "partial_update": ["member", "biz_edit"],
        "destroy": ["member", "admin"],
    }

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    serializer_class = BizSerializer


# Hours serializer views.
class HoursViewSet(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [HasGroupPermission]
    required_groups = {
        "list": ["__all__"],
        "create": ["member"],
        "upate": ["member"],
        "partial_update": ["member"],
        "destroy": ["member", "admin"],
    }

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    serializer_class = HoursSerializer
