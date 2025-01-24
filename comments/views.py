from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly

from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer


class CommentPagination(PageNumberPagination):
    page_size = 10


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for Comment model."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
    pagination_class = CommentPagination

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return CommentDetailSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        """Save the new comment instance with the current user as the owner."""
        serializer.save(owner=self.request.user)
