from django.contrib import admin

from .models import Album, Image


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username')
    list_filter = ('created_at', 'updated_at')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'album', 'created_at', 'likes_count')
    search_fields = ('caption', 'album__title')
    list_filter = ('created_at',)
    readonly_fields = ('likes_count',)

    def likes_count(self, obj):
        return obj.likes.count()

    likes_count.short_description = 'Likes Count'
