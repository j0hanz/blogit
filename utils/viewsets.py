import logging

from django.db import DatabaseError, IntegrityError
from rest_framework import serializers, viewsets
from rest_framework.response import Response

from utils.error_handling import ErrorHandler
from utils.mixins import DestroyMixin

logger = logging.getLogger(__name__)


class BaseViewSet(DestroyMixin, viewsets.ModelViewSet):
    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        """Create a new instance."""
        try:
            serializer.save(owner=self.request.user)
            self.log_action('create', serializer.instance)
        except IntegrityError as e:
            ErrorHandler.handle_integrity_error(e)
        except DatabaseError as e:
            ErrorHandler.handle_database_error(e)

    def perform_update(self, serializer: serializers.ModelSerializer) -> None:
        """Update an existing instance."""
        try:
            serializer.save()
            self.log_action('update', serializer.instance)
        except IntegrityError as e:
            ErrorHandler.handle_integrity_error(e)
        except DatabaseError as e:
            ErrorHandler.handle_database_error(e)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a single instance."""
        try:
            instance = self.get_object()
            self.log_action('retrieve', instance)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except DatabaseError as e:
            ErrorHandler.handle_database_error(e)

    def list(self, request, *args, **kwargs):
        """List all instances."""
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except DatabaseError as e:
            ErrorHandler.handle_database_error(e)

    def log_action(
        self, action: str, instance: serializers.ModelSerializer
    ) -> None:
        """Log an action performed on an instance."""
        logger.info(
            f'{self.__class__.__name__} {action} by {self.request.user.username}: {instance}'
        )
