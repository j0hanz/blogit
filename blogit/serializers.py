import logging

from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

logger = logging.getLogger(__name__)


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for the current authenticated user."""

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_picture = serializers.SerializerMethodField()

    def get_profile_picture(self, obj):
        profile_picture = getattr(obj.profile, 'profile_picture', None)
        if profile_picture:
            return profile_picture.url
        logger.error(f'Error retrieving profile picture for user {obj.id}')
        return None

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id',
            'profile_picture',
        )
