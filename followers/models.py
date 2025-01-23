from django.contrib.auth.models import User
from django.db import models

UNIQUE_FOLLOW_CONSTRAINT_NAME = 'unique_follow'


class Follower(models.Model):
    """Represents a user following another user."""

    owner: models.ForeignKey = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
    )
    followed: models.ForeignKey = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE,
    )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'followed'],
                name=UNIQUE_FOLLOW_CONSTRAINT_NAME,
            ),
        ]

    def __str__(self) -> str:
        return f'{self.owner} follows {self.followed}'
