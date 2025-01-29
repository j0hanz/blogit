from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin view for the Post model."""

    list_display = ['owner', 'created_at', 'views', 'is_published']
    search_fields = ['content']
    list_filter = ['created_at', 'updated_at', 'is_published']
    readonly_fields = ['created_at', 'updated_at']
