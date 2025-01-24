import logging

from django.db import DatabaseError, IntegrityError
from django.urls import reverse
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from blogit.permissions import IsOwnerOrReadOnly
from utils.viewsets import BaseViewSet

from .models import Follower
from .serializers import FollowerSerializer

logger = logging.getLogger(__name__)


class FollowerViewSet(BaseViewSet):
    """ViewSet for Follower model."""

    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    def perform_create(self, serializer: FollowerSerializer) -> None:
        """Save the new follower instance with the current user as the owner."""
        try:
            super().perform_create(serializer)
            logger.info(
                'Follower created: %s -> %s',
                self.request.user,
                serializer.instance.followed,
            )
            logger.info(
                'Follower URL: %s',
                reverse('follower-detail', args=[serializer.instance.id]),
            )
        except IntegrityError as err:
            logger.exception(
                'IntegrityError: possible duplicate follower',
            )
            raise ValidationError({'detail': 'possible duplicate'}) from err
        except DatabaseError as e:
            logger.error(f'Database error: {e}')
            raise
