from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models.account import Account
from accounts.models.admin import Admin
from accounts.models.coach import Coach
from accounts.models.member import Member
from accounts.models.visitor import Visitor
from authentication.serializers.signin import SignInSerializer


class SignIn(APIView):
    def is_authenticated(self, username: str, password: str) -> Account:
        account = Account.objects.filter(username=username, password=password).first()
        return account

    def get_account(self, account: Account):
        response = {}
        try:
            response["account"] = account.admin
            response["role"] = "admin"
        except Admin.DoesNotExist:
            pass

        try:
            response["account"] = account.coach
            response["role"] = "coach"
        except Coach.DoesNotExist:
            pass

        try:
            response["account"] = account.member
            response["role"] = "member"
        except Member.DoesNotExist:
            pass

        try:
            response["account"] = account.visitor
            response["role"] = "visitor"
        except Visitor.DoesNotExist:
            pass

        return response

    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")

            account = self.is_authenticated(username, password)

            response = {}
            if not account:
                response["error"] = "Invalid credentials."
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            if not account.is_active:
                response["error"] = "Account inactive."
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
            if account.is_verified:
                response["error"] = "Account not verified."
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
