from rest_framework import serializers
from utils.mixins import OwnerInfoMixin


class BaseSerializer(OwnerInfoMixin, serializers.ModelSerializer):
    """Base serializer with owner info mixin."""
