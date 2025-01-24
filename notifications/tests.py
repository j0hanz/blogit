from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from notifications.models import Notification

User = get_user_model()


class NotificationTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_notification(self) -> None:
        Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='test notification',
            target='1',
        )
        response = self.client.get('/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_mark_as_read(self) -> None:
        notification = Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='test notification',
            target='1',
        )
        response = self.client.post(
            f'/notifications/{notification.id}/mark_as_read/'
        )
        self.assertEqual(response.status_code, 204)
        notification.refresh_from_db()
        self.assertTrue(notification.read)

    def test_mark_all_as_read(self) -> None:
        Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='test notification 1',
            target='1',
        )
        Notification.objects.create(
            recipient=self.user,
            actor=self.user,
            verb='test notification 2',
            target='2',
        )
        response = self.client.post('/notifications/mark_all_as_read/')
        self.assertEqual(response.status_code, 204)
        self.assertTrue(
            Notification.objects.filter(
                recipient=self.user, read=True
            ).count(),
            2,
        )
