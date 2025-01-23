from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin view for the Post model."""

    list_display = ['owner', 'created_at']
    search_fields = ['content']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
