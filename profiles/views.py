import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from blogit.permissions import IsOwnerOrReadOnly

from .models import Profile
from .serializers import ProfileSerializer

logger = logging.getLogger(__name__)


class ProfileList(generics.ListAPIView):
    """View for listing profiles."""

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followers__created_at',
    ]
    search_fields = ['owner__username', 'name', 'bio']

    def get_queryset(self):
        try:
            return super().get_queryset()
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting profiles."""

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__posts', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            return super().get_object()
        except ObjectDoesNotExist as e:
            logger.error(f'Profile not found: {e}')
            raise
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise
