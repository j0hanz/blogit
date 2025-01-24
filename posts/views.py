from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for Post model."""

    queryset = Post.objects.select_related('owner').order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer: PostSerializer) -> None:
        """Save the new post instance with the current user as the owner."""
        serializer.save(owner=self.request.user)
