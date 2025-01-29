from blogit.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.viewsets import BaseViewSet

from likes.models import Like
from likes.serializers import LikeSerializer


class LikeViewSet(BaseViewSet):
    """ViewSet for Like model."""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
