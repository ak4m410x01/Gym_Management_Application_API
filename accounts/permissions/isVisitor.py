from rest_framework.permissions import BasePermission
from authentication.utils.token import JWTToken


class IsVisitor(BasePermission):
    def has_permission(self, request, view):
        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)
        return payload.get("user_role") == "visitor"

    def has_object_permission(self, request, view, obj):
        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)
        return payload.get("username") == obj.user.username
