from rest_framework.permissions import BasePermission
from authentication.utils.token import JWTToken


class IsSubscriptionOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)
        user_role = payload.get("user_role")
        if user_role == "coach":
            return obj.coach == payload.get("user_id")
        elif user_role == "member":
            return obj.member == payload.get("user_id")
        return False
