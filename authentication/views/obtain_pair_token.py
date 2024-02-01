from typing import Dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from authentication.serializers.obtain_pair_token import ObtainPairTokenSerializer
from accounts.models.user import User
from accounts.models.admin import Admin
from accounts.models.coach import Coach
from accounts.models.member import Member
from accounts.models.visitor import Visitor


class ObtainPairTokenView(APIView):
    permission_classes = (AllowAny,)

    def is_authenticated(self, username: str, password: str) -> User:
        return User.objects.filter(username=username, password=password).first()

    def get_user(self, user: User) -> Dict:
        response = {"user": None, "role": None}
        models = (
            (Admin, "admin"),
            (Coach, "coach"),
            (Member, "member"),
            (Visitor, "visitor"),
        )
        for model, role in models:
            try:
                response["user"] = getattr(user, model.__name__.lower()).user
                response["role"] = role
                break
            except model.DoesNotExist:
                pass
        return response

    def post(self, request) -> Response:
        serializer = ObtainPairTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")

            user = self.is_authenticated(username, password)

            response = {}
            if not user:
                response["error"] = "Invalid credentials."
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            if not user.is_active:
                response["error"] = "Account inactive."
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            if not user.is_verified:
                response["error"] = "Account not verified."
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

            user = self.get_user(user)
            token = RefreshToken.for_user(user.get("user"))
            token["username"] = username
            token["role"] = user.get("role")
            response["refresh_token"] = str(token)
            response["access_token"] = str(token.access_token)

            return Response(response, status=status.HTTP_200_OK)

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
