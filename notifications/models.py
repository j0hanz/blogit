from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Notification(models.Model):
    """Model to represent a notification."""

    recipient = models.ForeignKey(
        User, related_name='notifications', on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        User, related_name='actor_notifications', on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target}'
