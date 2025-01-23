from rest_framework import serializers

from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """Serializer for the Follower model"""

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed', 'followed_name']
