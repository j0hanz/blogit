from django.db import IntegrityError
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from blogit.permissions import IsOwnerOrReadOnly

from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """View for listing and creating followers."""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer) -> None:
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise ValidationError({'detail': 'possible duplicate'})


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """View for retrieving and deleting followers."""

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
