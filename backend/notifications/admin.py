from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'recipient',
        'actor',
        'verb',
        'target',
        'created_at',
        'read',
    )
    search_fields = (
        'recipient__username',
        'actor__username',
        'verb',
        'target',
    )
    list_filter = ('created_at', 'read')
