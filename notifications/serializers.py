from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for the Notification model."""

    actor_username = serializers.ReadOnlyField(source='actor.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')

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
            'created_at',
            'read',
        ]
        read_only_fields = ['created_at']
