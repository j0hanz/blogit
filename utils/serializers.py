from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj: object) -> bool:
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj: object) -> str:
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj: object) -> str:
        return naturaltime(obj.updated_at)
