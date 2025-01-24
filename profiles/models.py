from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    """User profile with personal info and image."""

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    profile_picture = CloudinaryField(
        'image', default='nobody_nrbk5n', blank=True
    )
    bio = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.owner.username}'s profile"

    def post_count(self) -> int:
        """Return the count of posts by the owner."""
        return self.owner.posts.count()


@receiver(post_save, sender=User)
def create_or_update_profile(
    sender: type, instance: User, created: bool, **kwargs: dict
) -> None:
    """Create or update profile when user is created or updated."""
    if created:
        Profile.objects.create(owner=instance)
    else:
        instance.profile.save()
