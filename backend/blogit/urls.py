"""URL Configuration."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .views import RootRoute

urlpatterns = [
    path('', RootRoute.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls'),
    ),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
    path('followers/', include('followers.urls')),
    path('likes/', include('likes.urls')),
    path('comments/', include('comments.urls')),
    path('notifications/', include('notifications.urls')),
    path('gallery/', include('gallery.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
