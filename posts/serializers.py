from django.utils.timesince import timesince
from rest_framework import serializers

from likes.models import Like

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""

    human_readable_created_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    def get_human_readable_created_at(self, obj):
        return timesince(obj.created_at)

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_user_has_liked(self, obj):
        user = self.context['request'].user
        return (
            user.is_authenticated
            and Like.objects.filter(owner=user, post=obj).exists()
        )

    def validate_content(self, value):
        if not value and not self.initial_data.get('image'):
            msg = 'You must upload an image or write some content.'
            raise serializers.ValidationError(msg)
        return value

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
            'like_id',
            'likes_count',
            'user_has_liked',
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']
