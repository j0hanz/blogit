import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.db.models import Count
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly
from utils.viewsets import BaseViewSet

from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)


class PostViewSet(BaseViewSet):
    """ViewSet for Post model."""

    queryset = (
        Post.objects.select_related('owner')
        .annotate(comments_count=Count('comments'))
        .order_by('-created_at')
    )
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'owner__username']

    def perform_create(self, serializer: PostSerializer) -> None:
        """Save the new post instance with the current user as the owner."""
        try:
            serializer.save(owner=self.request.user)
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise

    def get_queryset(self):
        try:
            return super().get_queryset()
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise

    def get_object(self):
        try:
            return super().get_object()
        except ObjectDoesNotExist as e:
            logger.error(f'Post not found: {e}')
            raise
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise
