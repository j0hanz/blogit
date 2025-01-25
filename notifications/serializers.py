from rest_framework import serializers

from utils.validation import validate_actor_and_recipient

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for the Notification model."""

    actor_username = serializers.ReadOnlyField(source='actor.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')
    image_url = serializers.ReadOnlyField(source='image.image.url')

    class Meta:
        model = Notification
        fields = [
            'id',
            'actor',
            'actor_username',
            'recipient',
            'recipient_username',
            'verb',
            'target',
            'image',
            'image_url',
            'created_at',
            'read',
        ]
        read_only_fields = ['created_at']

    def validate(self, data):
        return validate_actor_and_recipient(data)
