from django.db import DatabaseError, IntegrityError
from rest_framework import serializers, viewsets

from utils.error_handling import handle_database_error, handle_integrity_error


class BaseViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError as e:
            handle_integrity_error(e)
        except DatabaseError as e:
            handle_database_error(e)
