from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, serializers
from .models import Comment
from .serializers import CommentSerializer
from biz.permissions import HasGroupPermission

# Comment serializer views.


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    # authentication_classes = (authentication.TokenAuthentication,) /
    # Commented above live due to issues with simple-jwt package.
    permission_classes = [HasGroupPermission]
    required_groups = {
        "list": ["__all__"],
        "create": ["member"],
        "update": ["member", "admin"],
        "partial_update": ["member"],
        "destroy": ["member", "admin"],
    }

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        comment = self.get_object()
        if self.request.user == comment.user:
            return self.update(request, *args, **kwargs)
        else:
            msg = _("You can't edit other users' comments.")
            raise serializers.ValidationError(msg, code="authentication")
