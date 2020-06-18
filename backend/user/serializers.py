from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
# from django.core.mail import send_mail
from core.models import ActivationCode
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
            "is_staff",
            "phone",
            "member_since",
        )
        read_only_fields = [
            "id",
            "is_staff",
        ]

        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    # def get_full_name(self):
    #     """Gets full name of user"""
    #     return "%s %s" % (self.name, self.last_name)
    # These two functions must be tested and rewritten.
    # def get_short_name(self):
    #     """Gets user's first name"""
    #     return self.name

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        member_check = Group.objects.get_or_create(name="member")  # noqa: F841
        member_group = Group.objects.get(name="member")
        user = get_user_model().objects.create(**validated_data)
        user.is_active = False
        user.set_password(validated_data["password"])
        member_group.user_set.add(user)
        code = ActivationCode.objects.create(user=user)  # noqa F841
        # send_mail(
        #     'Activate Your Account',
        #     'Here is the activation code: %s' % code,
        #     'hoseyn.wanton@gmail.com',
        #     [user.email]
        # )
        user.save()
        return user

    def update(self, instance, validated_data):
        """Update a user, settin the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class ActivationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivationCode
        fields = (
            "code",
        )
