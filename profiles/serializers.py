from rest_framework import serializers

from followers.models import Follower

from .models import Profile

MAX_BIO_LENGTH = 500


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model."""

    post_count = serializers.IntegerField(read_only=True)
    profile_picture_url = serializers.ReadOnlyField(
        source='profile_picture.url'
    )
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    is_following = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user,
                followed=obj.owner,
            ).first()
            return following.id if following else None
        return None

    def get_is_following(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Follower.objects.filter(
                owner=user, followed=obj.owner
            ).exists()
        return False

    def validate_website(self, value):
        if value and not value.startswith('http'):
            msg = 'Website URL must start with http or https.'
            raise serializers.ValidationError(msg)
        return value

    def validate_bio(self, value):
        if len(value) > MAX_BIO_LENGTH:
            msg = f'Bio must be {MAX_BIO_LENGTH} characters or less.'
            raise serializers.ValidationError(msg)
        return value

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
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
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
