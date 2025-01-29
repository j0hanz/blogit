import logging

from blogit.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.queryset import annotate_post_queryset
from utils.viewsets import BaseViewSet

from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)


class PostViewSet(BaseViewSet):
    """ViewSet for Post model."""

    queryset = annotate_post_queryset(Post.objects.all())
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'owner__username']
