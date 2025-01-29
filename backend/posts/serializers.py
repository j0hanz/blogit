from gallery.serializers import ImageSerializer
from rest_framework import serializers
from utils.mixins import PostValidationMixin
from utils.serializers import BaseSerializer

from .models import Post

MAX_CONTENT_LENGTH = 500


class PostSerializer(BaseSerializer, PostValidationMixin):
    """Serializer for Post model."""

    human_readable_created_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    images = ImageSerializer(many=True, read_only=True, source='owner.images')
    is_published = serializers.BooleanField(default=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'content',
            'image',
            'views',
            'is_published',
            'created_at',
            'updated_at',
            'human_readable_created_at',
            'like_id',
            'likes_count',
            'comments_count',
            'images',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']
