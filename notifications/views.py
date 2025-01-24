from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blogit.permissions import IsOwnerOrReadOnly
from blogit.serializers import NotificationSerializer
from utils.viewsets import BaseViewSet

from .models import Notification


class NotificationViewSet(BaseViewSet):
    """ViewSet for the Notification model."""

    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        ).select_related('actor', 'recipient')

    @action(detail=False, methods=['post'])
    def mark_all_as_read(self, request):
        updated_count = self.get_queryset().update(read=True)
        return Response({'updated': updated_count}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.read = True
        notification.save()
        return Response(
            {'id': notification.id, 'read': notification.read},
            status=status.HTTP_200_OK,
        )
