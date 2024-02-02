from jwt import decode
from decouple import config

from rest_framework.permissions import BasePermission


class IsCoach(BasePermission):
    def has_permission(self, request, view):
        token = request.auth.token.decode()

        payload = decode(
            token,
            key=config("JWT_SECRET_KEY"),
            algorithms=["HS256"],
        )

        return payload.get("role") == "coach"
    
    def has_object_permission(self, request, view, obj):
        token = request.auth.token.decode()

        payload = decode(
            token,
            key=config("JWT_SECRET_KEY"),
            algorithms=["HS256"],
        )

        return payload.get("username") == obj.user.username

