from django.contrib.auth import get_user_model
from django.db import models

from gallery.models import Image


class Notification(models.Model):
    """Model to represent a notification."""

    recipient = models.ForeignKey(
        get_user_model(),
        related_name='notifications',
        on_delete=models.CASCADE,
    )
    actor = models.ForeignKey(
        get_user_model(),
        related_name='actor_notifications',
        on_delete=models.CASCADE,
    )
    verb = models.CharField(max_length=255)
    target = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        Image,
        related_name='notifications',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'{self.actor} {self.verb} {self.target}'
