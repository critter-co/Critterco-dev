from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


User = get_user_model()


class TestAuthentication(TestCase):
    """Test sign up, sign in, and self data request"""

    def test_api_jwt(self):
        """Creates a user"""
        url = reverse('user:create')
        u = User.objects.create_user(username='user', email='user@foo.com', password='user@foo.com')
        u.is_active = False
        u.save()
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

        """Creates a user with an email already existing in database"""
        resp = self.client.post(url, {'email': 'user@foo.com', 'password': 'user@foo.com'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        """Makes a post request to token url and obtains an access token."""
        verification_url = reverse('token_obtain_pair')
        resp = self.client.post(verification_url, {'email': 'user@foo.com',
                                                   'password': 'user@foo.com'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)

        token = resp.data['access']
        userurl = reverse('user:me')
        client = APIClient()

        """Request user data with an VALID token"""
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'abc')
        resp = client.get(userurl, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        """Requests user data with a VALID"""
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = client.get(userurl, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
