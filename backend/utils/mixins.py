import logging

from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.utils.timesince import timesince
from rest_framework import serializers

from followers.models import Follower
from likes.models import Like
from utils.error_handling import ErrorHandler
from utils.validation import Validator

logger = logging.getLogger(__name__)

MAX_BIO_LENGTH = 500


class ErrorHandlingMixin:
    """Mixin for handling errors."""

    def perform_create(self, serializer):
        """Save the new post instance with the current user as the owner."""
        try:
            serializer.save(owner=self.request.user)
        except DatabaseError as e:
            ErrorHandler.handle_generic_database_error(
                e, context='perform_create'
            )

    def get_queryset(self):
        """Get the queryset."""
        try:
            return super().get_queryset()
        except DatabaseError as e:
            ErrorHandler.handle_generic_database_error(
                e, context='get_queryset'
            )

    def get_object(self):
        """Get a single object."""
        try:
            return super().get_object()
        except ObjectDoesNotExist as e:
            ErrorHandler.handle_object_does_not_exist_error(e)
        except DatabaseError as e:
            ErrorHandler.handle_generic_database_error(e, context='get_object')


class DestroyMixin:
    """Mixin for handling destroy actions with logging and error handling."""

    def perform_destroy(self, instance):
        """Delete an instance with logging and error handling."""
        try:
            instance.delete()
            self.log_action('delete', instance)
            logger.info(
                f'{self.__class__.__name__} deleted by {self.request.user.username}'
            )
        except DatabaseError as e:
            ErrorHandler.handle_database_error(e)


class LoggingMixin:
    """Mixin for logging actions."""

    def perform_create(self, serializer):
        """Log creation of an instance."""
        super().perform_create(serializer)
        logger.info(
            f'{self.__class__.__name__} created by {self.request.user.username}'
        )

    def perform_update(self, serializer):
        """Log update of an instance."""
        super().perform_update(serializer)
        logger.info(
            f'{self.__class__.__name__} updated by {self.request.user.username}'
        )


class OwnerInfoMixin(serializers.ModelSerializer):
    """Mixin for adding owner info to serializers."""

    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj: object) -> bool:
        """Check if the current user is the owner."""
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj: object) -> str:
        """Get the creation time in human-readable format."""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj: object) -> str:
        """Get the update time in human-readable format."""
        return naturaltime(obj.updated_at)


class ProfileValidationMixin:
    """Mixin for validating profile data."""

    def get_following_id(self, obj: object) -> int | None:
        """Get the ID of the following relationship."""
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_is_following(self, obj: object) -> bool:
        """Check if the current user is following the owner."""
        user = self.context['request'].user
        return (
            user.is_authenticated
            and Follower.objects.filter(
                owner=user, followed=obj.owner
            ).exists()
        )

    def validate_website(self, value: str) -> str:
        """Validate the website URL."""
        if value and not value.startswith('http'):
            msg = 'Website URL must start with http or https.'
            raise serializers.ValidationError(msg)
        return value

    def validate_bio(self, value: str) -> str:
        """Validate the bio."""
        if len(value) > MAX_BIO_LENGTH:
            msg = f'Bio must be {MAX_BIO_LENGTH} characters or less.'
            raise serializers.ValidationError(msg)
        return value


class PostValidationMixin:
    """Mixin for validating post data."""

    def get_comments_count(self, obj: object) -> int:
        """Get the count of comments."""
        return obj.comments.count()

    def get_human_readable_created_at(self, obj: object) -> str:
        """Get the creation time in human-readable format."""
        return timesince(obj.created_at)

    def get_like_id(self, obj: object) -> int | None:
        """Get the ID of the like relationship."""
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj: object) -> int:
        """Get the count of likes."""
        return obj.likes.count()

    def validate_content(self, value: str) -> str:
        """Validate the content."""
        return Validator.validate_content(
            value, self.initial_data.get('image')
        )
