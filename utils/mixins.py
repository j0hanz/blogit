import logging

from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers

logger = logging.getLogger(__name__)


class LoggingMixin:
    def perform_create(self, serializer):
        super().perform_create(serializer)
        logger.info(
            f'{self.__class__.__name__} created by {self.request.user.username}'
        )

    def perform_update(self, serializer):
        super().perform_update(serializer)
        logger.info(
            f'{self.__class__.__name__} updated by {self.request.user.username}'
        )

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        logger.info(
            f'{self.__class__.__name__} deleted by {self.request.user.username}'
        )


class OwnerInfoMixin(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj: object) -> bool:
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj: object) -> str:
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj: object) -> str:
        return naturaltime(obj.updated_at)
