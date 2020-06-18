from rest_framework import generics, permissions, serializers, status
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import ActivationCode
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# User serializer views.


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class ConfirmCodeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        try:
            co = ActivationCode.objects.get(code=code)
            user_id = co.user_id
            user = get_user_model().objects.get(id=user_id)
            user.is_active = True
            user.save()
            co.delete()
            return Response(user.email, status=status.HTTP_200_OK)
        except ActivationCode.DoesNotExist:
            msg2 = _("Wrong code entered.")
            raise serializers.ValidationError(msg2, code="wrong")


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
