from django.utils.timesince import timesince
from rest_framework import serializers

from gallery.serializers import ImageSerializer
from likes.models import Like
from utils.serializers import BaseSerializer
from utils.validators import validate_content

from .models import Post

MAX_CONTENT_LENGTH = 500


class PostSerializer(BaseSerializer):
    """Serializer for Post model."""

    human_readable_created_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True, source='owner.images')
    is_published = serializers.BooleanField(default=True)

    def get_comments_count(self, obj: Post) -> int:
        return obj.comments.count()

    def get_human_readable_created_at(self, obj: Post) -> str:
        return timesince(obj.created_at)

    def get_like_id(self, obj: Post) -> int | None:
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj: Post) -> int:
        return obj.likes.count()

    def get_user_has_liked(self, obj: Post) -> bool:
        user = self.context['request'].user
        return (
            user.is_authenticated
            and Like.objects.filter(owner=user, post=obj).exists()
        )

    def validate_content(self, value: str) -> str:
        return validate_content(value, self.initial_data.get('image'))

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
            'user_has_liked',
            'comments_count',
            'images',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']
