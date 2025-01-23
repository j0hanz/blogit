from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Post


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
        return timesince(obj.created_at)

    def validate_content(self, value):
        if not value and not self.initial_data.get('image'):
            msg = 'You must upload an image or write some content.'
            raise serializers.ValidationError(
                msg
            )
        return value
