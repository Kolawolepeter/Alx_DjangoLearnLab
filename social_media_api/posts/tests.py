from django.test import TestCase
from django.contrib.auth import get_user_model

class FollowTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='user1', password='pass')
        self.user2 = get_user_model().objects.create_user(username='user2', password='pass')

    def test_follow_user(self):
        self.client.login(username='user1', password='pass')
        response = self.client.post(f'/api/follow/{self.user2.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user2, self.user1.following.all())
