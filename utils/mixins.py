import logging

from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from rest_framework import serializers

logger = logging.getLogger(__name__)


class ErrorHandlingMixin:
    def perform_create(self, serializer):
        """Save the new post instance with the current user as the owner."""
        try:
            serializer.save(owner=self.request.user)
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise

    def get_queryset(self):
        try:
            return super().get_queryset()
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise

    def get_object(self):
        try:
            return super().get_object()
        except ObjectDoesNotExist as e:
            logger.error(f'Object not found: {e}')
            raise
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise


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
