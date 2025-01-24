import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly
from utils.mixins import ErrorHandlingMixin, LoggingMixin
from utils.pagination import StandardResultsSetPagination
from utils.viewsets import BaseViewSet

from .models import Comment
from .serializers import CommentDetailSerializer, CommentSerializer

logger = logging.getLogger(__name__)


class CommentViewSet(ErrorHandlingMixin, LoggingMixin, BaseViewSet):
    """ViewSet for Comment model."""

    queryset = Comment.objects.select_related('owner', 'post').all()
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
