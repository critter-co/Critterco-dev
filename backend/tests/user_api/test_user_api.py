from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import ActivationCode

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('token_obtain_pair')
EDIT_USER_URL = reverse('user:me')
CONFIRM_CODE_URL = reverse('user:confirm')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test sign up API."""

    def setUp(self):
        self.client = APIClient()

    def test_api_create_user(self):
        """Test creating user through API."""
        payload = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'name': 'Test name',
            'first_name': 'fooname'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_created_user_is_member(self):
        """Test that when user is created they're added to member Group"""
        payload = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'name': 'Test name',
            'first_name': 'fooname'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        user = get_user_model().objects.get(**res.data)
        member_group = Group.objects.get(name="member").user_set.filter(id=user.id).exists()
        self.assertTrue(member_group)

    def test_user_exists(self):
        """Test creating a user that already exists fails."""
        payload = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'first_name': 'fooname'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_valid_email(self):
        """Test that user with a bad email isn't created."""
        payload = {
            'email': '@badmail.com',
            'password': 'testpassword',
            'name': 'Test name',
            'first_name': 'fooname'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters."""
        payload = {
            "email": 'test@bar.com',
            "password": "pw",
            'first_name': 'fooname'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token(self):
        """Test that user can get a token"""
        payload = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'first_name': 'fooname'
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given."""
        create_user(email='test@foo.com', password='testpassword')
        payload = {
            'email': 'test@foo.com',
            'password': 'wrongpassword',
            'first_name': 'fooname'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_no_user(self):
        """Test that token is not created if user doesn't exist."""
        payload = {
            "email": "test@foo.com",
            "password": "testpassword",
            'username': 'fooname'
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_missing_field(self):
        """Test that both email and password are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_update_password(self):
        """Test that user can update their password when they are logged in"""
        create_user(email='test@foo.com', password='testpassword', first_name='fooname')
        get_token = self.client.post(TOKEN_URL, {'email': 'test@foo.com',
                                                 'password': 'testpassword'}, format='json')
        token = get_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        res = self.client.patch(EDIT_USER_URL, {'password': 'newpassword'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        user = get_user_model().objects.get(email='test@foo.com')
        self.assertTrue(user.check_password('newpassword'))

    def test_user_deactive_at_signup(self):
        """Test that users are inactive upon signup"""
        payload_user = {
            'email': 'foo@foo.com',
            'password': 'testpassword',
            'first_name': 'foo',
            'username': 'foo'
        }
        self.client.post(CREATE_USER_URL, payload_user)
        user = get_user_model().objects.get(email='foo@foo.com')
        self.assertEqual(user.is_active, False)

    def test_activation_code_generation_signup(self):
        """Test that an activation code is generated at signup"""
        payload_user = {
            'email': 'foo@foo.com',
            'password': 'testpassword',
            'first_name': 'foo',
            'username': 'foo'
        }
        self.client.post(CREATE_USER_URL, payload_user)
        user = get_user_model().objects.get(email='foo@foo.com')
        res = ActivationCode.objects.get(user=user)
        self.assertTrue(res)

    def test_user_activates_with_emailed_code(self):
        """Test that users can activate their account with the code emailed to them"""
        payload_user = {
            'email': 'foo@foo.com',
            'password': 'testpassword',
            'first_name': 'foo',
            'username': 'foo'
        }
        self.client.post(CREATE_USER_URL, payload_user)
        user_id = get_user_model().objects.get(email='foo@foo.com').id
        code = ActivationCode.objects.get(user_id=user_id).code
        code_load = {
            'code': code
        }
        res = self.client.post(CONFIRM_CODE_URL, code_load)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        user_status = get_user_model().objects.get(email='foo@foo.com').is_active
        self.assertEqual(user_status, True)
