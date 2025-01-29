from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer
from utils.viewsets import BaseViewSet


class LikeViewSet(BaseViewSet):
    """ViewSet for Like model."""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
