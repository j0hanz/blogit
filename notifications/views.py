from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from blogit.permissions import IsOwnerOrReadOnly
from notifications.serializers import NotificationSerializer
from utils.viewsets import BaseViewSet

from .models import Notification


class NotificationViewSet(BaseViewSet):
    """ViewSet for the Notification model."""

    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self) -> QuerySet[Notification]:
        return Notification.objects.filter(
            recipient=self.request.user
        ).select_related('actor', 'recipient')

    @action(detail=False, methods=['post'])
    def mark_all_as_read(self, request: Request) -> Response:
        updated_count = self.get_queryset().update(read=True)
        return Response({'updated': updated_count}, status=HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request: Request, pk: int = None) -> Response:
        notification = self.get_object()
        notification.read = True
        notification.save()
        return Response(
            {'id': notification.id, 'read': notification.read},
            status=HTTP_200_OK,
        )
