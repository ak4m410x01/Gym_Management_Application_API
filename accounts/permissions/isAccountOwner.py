from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
