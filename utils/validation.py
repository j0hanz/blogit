from django.core.exceptions import ValidationError
from rest_framework import serializers

MAX_CONTENT_LENGTH = 500


def validate_actor_and_recipient(data):
    if data['actor'] == data['recipient']:
        msg = 'Actor and recipient cannot be the same.'
        raise serializers.ValidationError(msg)
    return data


def validate_followed_user(request_user, value):
    if request_user == value:
        msg = 'You cannot follow yourself.'
        raise serializers.ValidationError(msg)
    return value


def validate_content(value: str, image: str = None) -> str:
    """Validates the content length and presence of content or image."""
    if not value and not image:
        msg = 'You must upload an image or write some content.'
        raise ValidationError(msg)
    if len(value) > MAX_CONTENT_LENGTH:
        msg = f'Content cannot exceed {MAX_CONTENT_LENGTH} characters.'
        raise ValidationError(msg)
    return value
