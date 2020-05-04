from .models import Biz, Hours
from comments.models import Comment
from rest_framework import viewsets, permissions
from .serializers import BizSerializer, HoursSerializer
from comments.serializers import CommentSerializer

# Biz Viewset


class BizViewSet(viewsets.ModelViewSet):
    queryset = Biz.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BizSerializer


class HoursViewSet(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HoursSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
