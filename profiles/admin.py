from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'name',
        'website',
        'created_at',
        'updated_at',
    ]
    search_fields = ['owner__username', 'name']
