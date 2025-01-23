from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Represents a user's profile with personal information and an image."""

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.owner.username}'s profile"


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs) -> None:
    """Function to create or update a profile once a user is created or updated."""
    if created:
        Profile.objects.create(owner=instance)
    else:
        instance.profile.save()
