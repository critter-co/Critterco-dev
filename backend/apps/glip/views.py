from django.shortcuts import render

# Glip serializer views
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from apps.core.permissions import HasGroupPermission
from .models import Glip
from .serializers import GlipSerializer


class GlipViewSet(CacheResponseMixin, viewsets.ModelViewSet):

    queryset = Glip.objects.all()
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

    serializer_class = GlipSerializer
