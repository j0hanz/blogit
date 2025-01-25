from django.db import DatabaseError, IntegrityError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogit.permissions import IsOwnerOrReadOnly
from utils.error_handling import handle_database_error, handle_integrity_error
from utils.mixins import ErrorHandlingMixin, LoggingMixin

from .models import Album, Image
from .serializers import AlbumSerializer, ImageSerializer


class AlbumViewSet(ErrorHandlingMixin, LoggingMixin, viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError as e:
            handle_integrity_error(e)
        except DatabaseError as e:
            handle_database_error(e)


class ImageViewSet(ErrorHandlingMixin, LoggingMixin, viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError as e:
            handle_integrity_error(e)
        except DatabaseError as e:
            handle_database_error(e)
