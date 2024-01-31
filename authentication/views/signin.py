from typing import Dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from accounts.models.account import Account
from accounts.models.admin import Admin
from accounts.models.coach import Coach
from accounts.models.member import Member
from accounts.models.visitor import Visitor
from authentication.serializers.signin import SignInSerializer


class SignIn(APIView):
    permission_classes = (AllowAny,)

    def is_authenticated(self, username: str, password: str) -> Account:
        account = Account.objects.filter(username=username, password=password).first()
        return account

    def get_account(self, account: Account) -> Dict:
        response = {"account": None, "role": None}
        models = (
            (Admin, "admin"),
            (Coach, "coach"),
            (Member, "member"),
            (Visitor, "visitor"),
        )
        for model, role in models:
            try:
                response["account"] = getattr(account, model.__name__.lower())
                response["role"] = role
                break
            except model.DoesNotExist:
                pass
        return response

    def post(self, request) -> Response:
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")

            account = self.is_authenticated(username, password)

            response = {}
            if not account:
                response["error"] = "Invalid credentials."
            if not account.is_active:
                response["error"] = "Account inactive."
            if not account.is_verified:
                response["error"] = "Account not verified."

            if "error" in response:
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

            account = self.get_account(account)
            token = RefreshToken.for_user(account.get("account"))
            token["username"] = username
            token["role"] = account.get("role")
            response["refresh_token"] = str(token)
            response["access_token"] = str(token.access_token)
            return Response(response, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
