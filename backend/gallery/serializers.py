from rest_framework import serializers

from .models import Album, Image


class ImageSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(
        source='likes.count', read_only=True
    )
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            'id',
            'album',
            'image',
            'caption',
            'created_at',
            'likes_count',
            'is_liked',
        ]

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user.is_authenticated and obj.likes.filter(id=user.id).exists()


class AlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'images',
            'created_at',
            'updated_at',
        ]
