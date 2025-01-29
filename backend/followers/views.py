import logging

from blogit.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
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
