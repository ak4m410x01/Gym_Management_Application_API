from rest_framework.permissions import BasePermission
from decouple import config


class IsDeveloper(BasePermission):
    def has_permission(self, request, view):
        return config("IsDeveloperHasPermission", cast=bool)

    def has_object_permission(self, request, view, obj):
        return config("IsDeveloperHasObjectPermission", cast=bool)
