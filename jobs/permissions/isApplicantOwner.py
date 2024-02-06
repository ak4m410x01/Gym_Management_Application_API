from rest_framework.permissions import BasePermission
from authentication.utils.token import JWTToken


class IsApplicantOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)
        return payload.get("username") == obj.applicant.username
