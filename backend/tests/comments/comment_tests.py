from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from apps.comments.models import Comment
from unittest.mock import MagicMock, patch

COMMENT_URL = reverse('comment-list')
# COMMENT_DETAIL_URL = reverse('comment-detail', args=comment.pk)
CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('token_obtain_pair')
User = get_user_model()


def create_user(**params):
    return get_user_model().objects.create_user(**params)


@patch('backend.celery_app.send_email_task', new=MagicMock())
class TestPatchComments(TestCase):
    """Tests for comment functions"""

    def setUp(self):
        self.client = APIClient()

    def test_comment_notallowed_with_session_login(self):
        """Test that posting comments with session login is not allowed."""
        payload = {
            'content': 'Test 1'
        }
        create_user(email="foo@test.com", password="testpassword", first_name="fooname")
        self.client.login(email="foo@test.com", password="testpassword")
        res = self.client.post(COMMENT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_comment_valid_token(self):
        """Test that a user with valid token can post comments."""
        payload_user = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'first_name': 'bar'
        }
        res = self.client.post(CREATE_USER_URL, payload_user)
        u = get_user_model().objects.get(email='foo@test.com')
        u.is_active = True
        u.save()
        get_token = self.client.post(TOKEN_URL, payload_user, format='json')
        token = get_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        payload = {
            'content': 'Test 1'
        }
        res = self.client.post(COMMENT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_created_comment_has_user_id(self):
        """Test that when user creates comment their user ID is in 'user' field of comment"""
        payload_user = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'first_name': 'bar'
        }
        self.client.post(CREATE_USER_URL, payload_user)
        u = get_user_model().objects.get(email='foo@test.com')
        u.is_active = True
        u.save()
        get_token = self.client.post(TOKEN_URL, payload_user, format='json')
        token = get_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        payload = {
            'content': 'Test 1'
        }
        self.client.post(COMMENT_URL, payload)
        user = get_user_model().objects.get(email="foo@test.com")
        user_id = user.id
        comment = Comment.objects.latest('id')
        comment_id = comment.user.id
        self.assertEqual(comment_id, user_id)

    def test_comment_partial_update(self):
        """Test that users can update(edit) their own comments after they are created"""
        payload_user = {
            'email': 'foo@test.com',
            'password': 'testpassword',
            'first_name': 'bar'
        }
        res = self.client.post(CREATE_USER_URL, payload_user)
        u = get_user_model().objects.get(email='foo@test.com')
        u.is_active = True
        u.save()
        get_token = self.client.post(TOKEN_URL, payload_user, format='json')
        token = get_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        payload = {
            'content': 'Test 1'
        }
        self.client.post(COMMENT_URL, payload)
        comment = Comment.objects.latest('id')
        res = self.client.patch(reverse('comment-detail', args=[comment.pk]), {'content': 'EDITED'})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        new_comment = Comment.objects.latest('id').content
        self.assertEqual(new_comment, 'EDITED')

    def test_edit_others_comment(self):
        """Test that users can't edit other users' comments.'"""
        payload_user = {
            'email': 'foo@foo.com',
            'password': 'testpassword',
            'first_name': 'foo',
            'username': 'foo'
        }
        res = self.client.post(CREATE_USER_URL, payload_user)
        u = get_user_model().objects.get(email='foo@foo.com')
        u.is_active = True
        u.save()
        get_token = self.client.post(TOKEN_URL, payload_user, format='json')
        token = get_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        payload = {
            'content': 'ORIGINAL'
        }
        self.client.post(COMMENT_URL, payload)
        comment = Comment.objects.latest('id')
        self.client.credentials()
        payload_user2 = {
            'email': 'bar@bar.com',
            'password': 'testpassword',
            'first_name': 'bar',
            'username': 'bar'
        }
        self.client.post(CREATE_USER_URL, payload_user2)
        u = get_user_model().objects.get(email='bar@bar.com')
        u.is_active = True
        u.save()
        get_token2 = self.client.post(TOKEN_URL, payload_user2, format='json')
        token2 = get_token2.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token2)
        res = self.client.patch(reverse('comment-detail', args=[comment.pk]), {'content': 'EDITED'})
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        new_comment = Comment.objects.latest('id').content
        self.assertEqual(new_comment, 'ORIGINAL')

    def test_comment_str(self):
        comment = Comment.objects.create(content='Test Comment')
        self.assertEqual(str(comment), 'Test Comment')
