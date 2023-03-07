from rest_framework import permissions


class AdminUserOrOwnerOrReadOnly(permissions.IsAdminUser):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            True
        return bool(request.user and request.user.is_staff or obj.id == request.user.id)
