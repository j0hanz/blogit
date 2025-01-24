from django.db.models.signals import post_save
from django.dispatch import receiver

from comments.models import Comment
from followers.models import Follower
from likes.models import Like
from notifications.models import Notification


@receiver(post_save, sender=Like)
def create_like_notification(
    sender: type, instance: Like, created: bool, **kwargs: dict
) -> None:
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,
            actor=instance.owner,
            verb='liked your post',
            target=instance.post.id,
        )


@receiver(post_save, sender=Follower)
def create_follower_notification(
    sender: type, instance: Follower, created: bool, **kwargs: dict
) -> None:
    if created:
        Notification.objects.create(
            recipient=instance.followed,
            actor=instance.owner,
            verb='started following you',
            target=instance.id,
        )


@receiver(post_save, sender=Comment)
def create_comment_notification(
    sender: type, instance: Comment, created: bool, **kwargs: dict
) -> None:
    if created:
        Notification.objects.create(
            recipient=instance.post.owner,
            actor=instance.owner,
            verb='commented on your post',
            target=instance.post.id,
        )
