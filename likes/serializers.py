import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import serializers

from likes.models import Like
from utils.validation import validate_like_post

logger = logging.getLogger(__name__)


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model."""

    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data: dict) -> Like:
        try:
            return super().create(validated_data)
        except IntegrityError as err:
            logger.exception('IntegrityError: possible duplicate like')
            raise ValidationError({'detail': 'possible duplicate'}) from err

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']
        read_only_fields = ['created_at']

    def validate_post(self, value):
        return validate_like_post(self.context['request'].user, value)
