from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers

from .models import Comment

MAX_CONTENT_LENGTH = 500


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for the Comment model."""

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_content(self, value):
        if not value:
            msg = 'Content cannot be empty.'
            raise serializers.ValidationError(msg)
        if len(value) > MAX_CONTENT_LENGTH:
            msg = f'Content cannot exceed {MAX_CONTENT_LENGTH} characters.'
            raise serializers.ValidationError(msg)
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

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
            'created_at',
            'updated_at',
        ]


class CommentDetailSerializer(CommentSerializer):
    """Serializer for detailed view of the Comment model."""

    post = serializers.ReadOnlyField(source='post.id')
