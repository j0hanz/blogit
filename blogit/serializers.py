from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for the current authenticated user."""

    profile_id = serializers.ReadOnlyField(source='profile.id')

    class Meta(UserDetailsSerializer.Meta):
        fields = (
            *UserDetailsSerializer.Meta.fields,
            'profile_id',
        )
