from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification
from utils.validators import validate_content

User = get_user_model()
MAX_CONTENT_LENGTH = 500


class Post(models.Model):
    """Blog post with image and content."""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    content = models.TextField(max_length=MAX_CONTENT_LENGTH, blank=True)
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return f'Post by {self.owner.username} at {self.created_at}'

    def comments_count(self) -> int:
        return self.comments.count()

    def clean(self) -> None:
        validate_content(self.content, self.image)

    @receiver(post_save, sender='posts.Post')
    def create_post_notification(
        self: type,
        instance: 'Post',
        created: bool,
        **kwargs: dict,
    ) -> None:
        if created:
            Notification.objects.create(
                recipient=instance.owner,
                actor=instance.owner,
                verb='created a new post',
                target=instance.id,
            )
