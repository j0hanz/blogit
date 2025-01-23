from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from blogit.permissions import IsOwnerOrReadOnly

from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """List all profiles."""

    queryset = (
        Profile.objects.annotate(
            posts_count=Count('owner__posts', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True),
        )
        .select_related('owner')
        .order_by('-created_at')
    )
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
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


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a profile."""

    permission_classes = [IsOwnerOrReadOnly]
    queryset = (
        Profile.objects.annotate(
            posts_count=Count('owner__posts', distinct=True),
            followers_count=Count('owner__followed', distinct=True),
            following_count=Count('owner__following', distinct=True),
        )
        .select_related('owner')
        .order_by('-created_at')
    )
    serializer_class = ProfileSerializer
