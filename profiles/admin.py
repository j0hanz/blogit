from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'created_at', 'updated_at')
    search_fields = ('owner__username', 'name')
    list_filter = ('created_at', 'updated_at')
