from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Blog post with image and content."""

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    content = models.TextField(max_length=500, blank=True)
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return f'Post by {self.owner.username} at {self.created_at}'

    def clean(self):
        if not self.content and not self.image:
            msg = 'You must upload an image or write some content.'
            raise ValidationError(msg)
