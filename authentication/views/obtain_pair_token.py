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

    def isAuthenticated(self, username: str, password: str) -> User:
        return User.objects.filter(username=username, password=password).first()

    def get_user(self, user: User) -> Dict:
        response = {"user_id": None, "user_obj": None, "user_role": None}
        USER_MODELS = (
            (Admin, "admin"),
            (Coach, "coach"),
            (Member, "member"),
            (Visitor, "visitor"),
        )

        for model, role in USER_MODELS:
            try:
                user = getattr(user, model.__name__.lower())

                response["user_id"] = user.id
                response["user_obj"] = user.user
                response["user_role"] = role
                break

            except model.DoesNotExist:
                pass

        return response

    def obtain_token(self, user: Dict):
        token = RefreshToken.for_user(user.get("user_obj"))

        token["user_id"] = user.get("user_id")
        token["user_role"] = user.get("user_role")

        return token

    def post(self, request) -> Response:
        serializer = ObtainPairTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")

            user = self.isAuthenticated(username, password)

            if not user:
                return Response(
                    {"error": "Invalid credentials."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            if not user.is_active:
                return Response(
                    {"error": "Account inactive."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            if not user.is_verified:
                return Response(
                    {"error": "Account not verified."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token = self.obtain_token(self.get_user(user))

            return Response(
                {
                    "access": f"{token.access_token}",
                    "refresh": f"{token}",
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )
