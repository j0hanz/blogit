from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Album(models.Model):
    """Model to represent an album of images."""

    owner = models.ForeignKey(
        User, related_name='albums', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Image(models.Model):
    """Model to represent an image in an album."""

    album = models.ForeignKey(
        Album, related_name='images', on_delete=models.CASCADE
    )
    image = CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='liked_images', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.caption if self.caption else 'Image'
