from rest_framework import serializers

from gallery.serializers import AlbumSerializer
from utils.mixins import ProfileValidationMixin
from utils.serializers import BaseSerializer

from .models import Profile

MAX_BIO_LENGTH = 500


class ProfileSerializer(BaseSerializer, ProfileValidationMixin):
    """Serializer for Profile model."""

    posts_count = serializers.IntegerField(read_only=True)
    profile_picture_url = serializers.ReadOnlyField(
        source='profile_picture.url',
    )
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    is_following = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    owner_username = serializers.ReadOnlyField(source='owner.username')
    albums = AlbumSerializer(many=True, read_only=True, source='owner.albums')

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'owner_username',
            'name',
            'profile_picture_url',
            'profile_picture',
            'bio',
            'website',
            'posts_count',
            'following_id',
            'followers_count',
            'following_count',
            'is_following',
            'albums',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
