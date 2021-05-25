import random
import string
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        user.is_active = False
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        # Checks if admin group exists, creates if not, and then adds user.
        Group.objects.get_or_create(name="admin")
        admin_group = Group.objects.get(name="admin")
        admin_group.user_set.add(user)
        # Checks if member group exists, creates if not, and then adds user.
        member_check = Group.objects.get_or_create(name="member")  # noqa: F841
        member_group = Group.objects.get(name="member")
        member_group.user_set.add(user)
        user.save(using=self._db)

        return user


phone_regex = RegexValidator(
    regex=r"^09\d{2}\d{7}$",
    message="Phone number must be entered in the following format: '09123456789'.",
)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support email, phonenumber, etc."""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(
        validators=[phone_regex], max_length=11, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    member_since = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    objects = UserManager()
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    USERNAME_FIELD = "email"


def generate_activation_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))


class ActivationCode(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    code = models.CharField(max_length=6, default=generate_activation_code)
