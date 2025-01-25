import logging

from django.db import DatabaseError, IntegrityError
from django.urls import reverse
from rest_framework import permissions

from blogit.permissions import IsOwnerOrReadOnly
from utils.error_handling import handle_database_error, handle_integrity_error
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

    def perform_create(self, serializer: FollowerSerializer) -> None:
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
            handle_integrity_error(err)
        except DatabaseError as e:
            handle_database_error(e)
