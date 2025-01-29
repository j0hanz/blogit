import logging

from blogit.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from utils.mixins import ErrorHandlingMixin
from utils.queryset import annotate_profile_queryset

from .models import Profile
from .serializers import ProfileSerializer

logger = logging.getLogger(__name__)


class ProfileList(ErrorHandlingMixin, generics.ListAPIView):
    """View for listing profiles."""

    queryset = annotate_profile_queryset(Profile.objects.all())
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


class ProfileDetail(ErrorHandlingMixin, generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting profiles."""

    permission_classes = [IsOwnerOrReadOnly]
    queryset = annotate_profile_queryset(Profile.objects.all())
    serializer_class = ProfileSerializer
