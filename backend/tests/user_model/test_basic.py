from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase, force_authenticate
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('token_obtain_pair')
EDIT_USER_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


def create_superuser(**params):
    return get_user_model().objects.create_superuser(**params)


class CustomUserModelTests(TestCase):
    """Test UserManager in user models functions."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email="foo@test.com", password='testpassword')
        self.superuser = create_superuser(email="test@test.com", password="testpassword")

    def test_user_create(self):
        """Test that create_user function works"""
        self.assertEqual(self.user.email, 'foo@test.com')

    def test_create_super_user(self):
        """Test that create_superuser function works"""
        self.assertEqual(self.superuser.is_superuser, True)
