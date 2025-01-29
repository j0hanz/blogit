from django.core.exceptions import ValidationError
from rest_framework import serializers

MAX_CONTENT_LENGTH = 500


class Validator:
    """Class containing various validation methods."""

    @staticmethod
    def validate_actor_and_recipient(data):
        """Validate that actor and recipient are not the same."""
        if data['actor'] == data['recipient']:
            msg = 'Actor and recipient cannot be the same.'
            raise serializers.ValidationError(msg)
        return data

    @staticmethod
    def validate_followed_user(request_user, value):
        """Validate that a user is not following themselves."""
        if request_user == value:
            msg = 'You cannot follow yourself.'
            raise serializers.ValidationError(msg)
        return value

    @staticmethod
    def validate_content(value: str, image: str = None) -> str:
        """Validate the content length and presence of content or image."""
        if not value and not image:
            msg = 'You must upload an image or write some content.'
            raise ValidationError(msg)
        if len(value) > MAX_CONTENT_LENGTH:
            msg = f'Content cannot exceed {MAX_CONTENT_LENGTH} characters.'
            raise ValidationError(msg)
        return value
