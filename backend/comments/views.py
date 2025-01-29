import logging

from blogit.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.pagination import StandardResultsSetPagination
from utils.queryset import annotate_comment_queryset
from utils.viewsets import BaseViewSet

from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer

logger = logging.getLogger(__name__)


class CommentViewSet(BaseViewSet):
    """ViewSet for Comment model."""

    queryset = annotate_comment_queryset(Comment.objects.all())
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self) -> type:
        return (
            CommentDetailSerializer
            if self.action in ['retrieve', 'update', 'partial_update']
            else CommentSerializer
        )
