from rest_framework import serializers

from followers.models import Follower
from gallery.serializers import AlbumSerializer
from utils.serializers import BaseSerializer

from .models import Profile

MAX_BIO_LENGTH = 500


class ProfileSerializer(BaseSerializer):
    """Serializer for Profile model."""

    post_count = serializers.IntegerField(read_only=True)
    profile_picture_url = serializers.ReadOnlyField(
        source='profile_picture.url',
    )
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    is_following = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    owner_username = serializers.ReadOnlyField(source='owner.username')
    albums = AlbumSerializer(many=True, read_only=True, source='owner.albums')

    def get_following_id(self, obj: Profile) -> int | None:
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner,
            ).first()
            return following.id if following else None
        return None

    def get_is_following(self, obj: Profile) -> bool:
        user = self.context['request'].user
        return (
            user.is_authenticated
            and Follower.objects.filter(
                owner=user,
                followed=obj.owner,
            ).exists()
        )

    def validate_website(self, value: str) -> str:
        if value and not value.startswith('http'):
            msg = 'Website URL must start with http or https.'
            raise serializers.ValidationError(msg)
        return value

    def validate_bio(self, value: str) -> str:
        if len(value) > MAX_BIO_LENGTH:
            msg = f'Bio must be {MAX_BIO_LENGTH} characters or less.'
            raise serializers.ValidationError(msg)
        return value

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
            'post_count',
            'following_id',
            'followers_count',
            'following_count',
            'is_following',
            'albums',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
