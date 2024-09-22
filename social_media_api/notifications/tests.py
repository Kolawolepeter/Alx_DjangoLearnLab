from django.test import TestCase
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.auth import get_user_model

class LikeTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='user1', password='pass')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Test Content')

    def test_like_post(self):
        self.client.login(username='user1', password='pass')
        response = self.client.post(f'/api/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Like.objects.filter(user=self.user, post=self.post).exists())

    def test_notification_created_on_like(self):
        self.client.login(username='user1', password='pass')
        self.client.post(f'/api/posts/{self.post.id}/like/')
        notification = Notification.objects.filter(recipient=self.post.author, verb='liked your post').first()
        self.assertIsNotNone(notification)
