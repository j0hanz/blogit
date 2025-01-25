from django.db import DatabaseError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer
from utils.error_handling import handle_database_error
from utils.mixins import ErrorHandlingMixin, LoggingMixin
from utils.viewsets import BaseViewSet


class LikeViewSet(ErrorHandlingMixin, LoggingMixin, BaseViewSet):
    """ViewSet for Like model."""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except DatabaseError as e:
            handle_database_error(e)
