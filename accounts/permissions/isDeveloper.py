from rest_framework.permissions import BasePermission


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False
