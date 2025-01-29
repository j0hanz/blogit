from gallery.serializers import ImageSerializer
from rest_framework import serializers
from utils.serializers import BaseSerializer
from utils.validation import Validator

from .models import Comment


class CommentSerializer(BaseSerializer):
    """Serializer for the Comment model."""

    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    image = ImageSerializer(read_only=True)

    def validate_content(self, value: str) -> str:
        """Validate the content of the comment."""
        return Validator.validate_content(value)

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'post',
            'content',
            'image',
            'created_at',
            'updated_at',
        ]


class CommentDetailSerializer(CommentSerializer):
    """Serializer for detailed view of the Comment model."""

    post = serializers.ReadOnlyField(source='post.id')
