from rest_framework import generics

from blogit.permissions import IsOwnerOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """List and create posts. Only authenticated users can create posts."""

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a post. Only the owner can modify it."""

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Post.objects.order_by('-created_at')
