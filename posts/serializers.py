from datetime import UTC, datetime, timedelta

from rest_framework import serializers

from .models import Post


def shortnaturaltime(value):
    """Return a human-readable string for the time delta from now to the given value."""
    now = datetime.now(UTC)
    delta = now - value

    if delta < timedelta(minutes=1):
        return 'just now'
    if delta < timedelta(hours=1):
        return f'{int(delta.total_seconds() // 60)}m'
    if delta < timedelta(days=1):
        return f'{int(delta.total_seconds() // 3600)}h'
    return f'{delta.days}d'


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""

    human_readable_created_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'content',
            'image',
            'created_at',
            'updated_at',
            'human_readable_created_at',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_human_readable_created_at(self, obj):
        return shortnaturaltime(obj.created_at)

    def validate_content(self, value):
        if not value and not self.initial_data.get('image'):
            msg = 'You must upload an image or write some content.'
            raise serializers.ValidationError(msg)
        return value
