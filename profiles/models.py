from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """Represents a user's profile with personal information."""

    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self) -> str:
        return f"{self.owner.username}'s profile"

    @receiver(models.signals.post_save, sender=User)
    def create_or_save_profile(sender, instance, created, **kwargs) -> None:
        """Create or save the profile when the user is created or saved."""
        if created:
            Profile.objects.create(owner=instance)
        else:
            instance.profile.save()

    def get_age(self) -> int:
        """Calculate the age of the user based on the birth date."""
        if self.birth_date:
            today = date.today()
            return (
                today.year
                - self.birth_date.year
                - (
                    (today.month, today.day)
                    < (self.birth_date.month, self.birth_date.day)
                )
            )
        return None

    def get_full_name(self) -> str:
        """Return the full name of the user."""
        return f'{self.owner.first_name} {self.owner.last_name}'.strip()
