from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to allow only owners to edit objects, while read access is unrestricted."""

    def has_object_permission(self, request, view, obj):
        """Check if the request has object-level permission."""
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'owner'):
            return obj.owner == request.user

        return False
