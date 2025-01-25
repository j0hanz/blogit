import logging

from django.db import DatabaseError
from rest_framework import permissions

from blogit.permissions import IsOwnerOrReadOnly
from utils.error_handling import handle_database_error
from utils.mixins import ErrorHandlingMixin, LoggingMixin
from utils.viewsets import BaseViewSet

from .models import Follower
from .serializers import FollowerSerializer

logger = logging.getLogger(__name__)


class FollowerViewSet(ErrorHandlingMixin, LoggingMixin, BaseViewSet):
    """ViewSet for Follower model."""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except DatabaseError as e:
            handle_database_error(e)
