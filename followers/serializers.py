from django.db import IntegrityError
from rest_framework import serializers

from utils.error_handling import ErrorHandler
from utils.validation import Validator

from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """Serializer for the Follower model"""

    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed', 'followed_name']

    def create(self, validated_data: dict) -> Follower:
        try:
            return super().create(validated_data)
        except IntegrityError as err:
            ErrorHandler.handle_integrity_error(err)

    def validate_followed(self, value):
        request_user = self.context['request'].user
        return Validator.validate_followed_user(request_user, value)
