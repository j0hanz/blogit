from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'bio',
            'location',
            'birth_date',
            'website',
            'created_at',
            'updated_at',
            'get_age',
            'get_full_name',
        ]
        read_only_fields = [
            'owner',
            'created_at',
            'updated_at',
            'get_age',
            'get_full_name',
        ]
