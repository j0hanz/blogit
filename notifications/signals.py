from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post

from .models import Notification


@receiver(post_save, sender=Post)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=getattr(instance, 'recipient', None),
            actor=getattr(instance, 'actor', None),
            verb='created a new post',
            target=instance.id,
        )
