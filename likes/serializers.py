import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import serializers

from likes.models import Like

logger = logging.getLogger(__name__)


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError as err:
            logger.error(
                'IntegrityError: possible duplicate like', exc_info=True
            )
            raise ValidationError({'detail': 'possible duplicate'}) from err
