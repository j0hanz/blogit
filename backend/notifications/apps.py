from django.apps import AppConfig
from django.db.models.signals import post_migrate


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self) -> None:
        from utils.signals import create_default_notifications

        post_migrate.connect(create_default_notifications, sender=self)
