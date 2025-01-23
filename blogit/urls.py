"""URL configuration."""

from django.contrib import admin
from django.urls import include, path

from .views import root_route

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/', include('profiles.urls')),
]
