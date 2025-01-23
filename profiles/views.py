from rest_framework import generics

from blogit.permissions import IsOwnerOrReadOnly

from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """View for listing profiles."""

    queryset = Profile.objects.order_by('-created_at')
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting profiles."""

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.order_by('-created_at')
    serializer_class = ProfileSerializer
