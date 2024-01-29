from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models.visitor import Visitor
from authentication.serializers.signup import SignUpSerializer
from authentication.serializers.signin import SignInSerializer


class SignUp(CreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = SignUpSerializer


class SignIn(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_200_OK)

        return Response(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
