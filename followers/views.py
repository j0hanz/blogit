import logging

from django.db import IntegrityError
from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer

from blogit.permissions import IsOwnerOrReadOnly

from .models import Follower
from .serializers import FollowerSerializer

logger = logging.getLogger(__name__)


class FollowerViewSet(viewsets.ModelViewSet):
    """ViewSet for Follower model."""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer: Serializer) -> None:
        """Save the new follower instance with the current user as the owner."""
        try:
            serializer.save(owner=self.request.user)
            logger.info(
                f'Follower created: {self.request.user} -> {serializer.instance.followed}'
            )
        except IntegrityError:
            logger.error('IntegrityError: possible duplicate follower')
            raise ValidationError({'detail': 'possible duplicate'})
