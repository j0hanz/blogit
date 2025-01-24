import logging

from django.db import IntegrityError
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

    def perform_create(self, serializer):
        """Save the new follower instance with the current user as the owner."""
        try:
            super().perform_create(serializer)
            logger.info(
                f'Follower created: {self.request.user} -> {serializer.instance.followed}'
            )
            follow_url = reverse(
                'follower-detail', args=[serializer.instance.id]
            )
            logger.info(f'Follower URL: {follow_url}')
        except IntegrityError as err:
            logger.error(
                'IntegrityError: possible duplicate follower', exc_info=True
            )
            raise ValidationError({'detail': 'possible duplicate'}) from err
