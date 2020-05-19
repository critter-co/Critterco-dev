from biz.models import Biz, Hours
from comments.models import Comment
from rest_framework import viewsets, permissions, authentication
from biz.serializers import BizSerializer, HoursSerializer
from comments.serializers import CommentSerializer
from biz.permissions import HasGroupPermission

# Biz Viewset


class BizViewSet(viewsets.ModelViewSet):
    queryset = Biz.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [HasGroupPermission]
    required_groups = {
        "GET": ["__all__"],
        "POST": ["member", "biz_post"],
        "PUT": ["member", "biz_edit"],
        "PATCH": ["member", "biz_edit"],
    }

    serializer_class = BizSerializer


class HoursViewSet(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HoursSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
