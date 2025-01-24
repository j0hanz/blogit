from django.db.models import Count
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
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
        serializer.save(owner=self.request.user)
