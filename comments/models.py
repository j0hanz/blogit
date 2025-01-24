from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from posts.models import Post

MAX_CONTENT_LENGTH = 500


class Comment(models.Model):
    """Represents a comment made by a user on a specific post."""

    owner = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.content[:20]

    def clean(self):
        if not self.content:
            msg = 'Content cannot be empty.'
            raise ValidationError(msg)
        if len(self.content) > MAX_CONTENT_LENGTH:
            msg = f'Content cannot exceed {MAX_CONTENT_LENGTH} characters.'
            raise ValidationError(msg)
