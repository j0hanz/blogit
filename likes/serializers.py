import logging

from django.db import IntegrityError
from rest_framework import serializers

from likes.models import Like
from utils.error_handling import handle_integrity_error

logger = logging.getLogger(__name__)


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for the Like model."""

    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data: dict) -> Like:
        try:
            return super().create(validated_data)
        except IntegrityError as err:
            handle_integrity_error(err)

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']
        read_only_fields = ['created_at']
