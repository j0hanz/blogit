from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for the current authenticated user.
    Extends the user details with profile-related fields.
    """

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_picture = serializers.SerializerMethodField()

    def get_profile_picture(self, obj):
        # Safely retrieves profile picture URL, returns None if unavailable
        return getattr(
            getattr(obj.profile, 'profile_picture', None), 'url', None
        )

    class Meta(UserDetailsSerializer.Meta):
        fields = (
            *UserDetailsSerializer.Meta.fields,
            'profile_id',
            'profile_picture',
        )
