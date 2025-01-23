from django.contrib import admin

from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    """Admin view for managing Follower instances."""

    list_display = ('owner', 'followed', 'created_at')
    search_fields = ('owner__username', 'followed__username')
    list_filter = ('created_at',)


# Register your models here.
