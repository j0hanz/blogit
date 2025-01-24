from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        post_migrate.connect(create_default_notifications, sender=self)


@receiver(post_migrate)
def create_default_notifications(sender, **kwargs):
    from notifications.models import Notification

    Notification.objects.get_or_create(
        recipient_id=1,
        actor_id=1,
        verb='default notification',
        target='1',
    )
