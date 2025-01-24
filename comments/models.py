from django.contrib.auth import get_user_model
from django.db import models

from posts.models import Post
from utils.validators import validate_content

User = get_user_model()


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
        validate_content(self.content)
