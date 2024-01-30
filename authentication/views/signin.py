from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models.account import Account
from authentication.serializers.signin import SignInSerializer


class SignIn(APIView):
    def is_authenticated(self, username: str, password: str) -> Account:
        account = Account.objects.filter(username=username, password=password).first()
        return account

    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            account = self.is_authenticated(username, password)
            if account:
                return Response(
                    {"detail": "valid credentials"},
                    status=status.HTTP_200_OK,
                )

        return Response(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
