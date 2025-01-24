from rest_framework import serializers, viewsets


class BaseViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        serializer.save(owner=self.request.user)
