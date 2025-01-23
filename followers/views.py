from django.db import IntegrityError
from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from blogit.permissions import IsOwnerOrReadOnly

from .models import Follower
from .serializers import FollowerSerializer


class FollowerViewSet(viewsets.ModelViewSet):
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
        except IntegrityError:
            raise ValidationError({'detail': 'possible duplicate'})
