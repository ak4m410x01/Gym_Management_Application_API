from rest_framework.generics import CreateAPIView

from accounts.models.visitor import Visitor
from authentication.serializers.signup import SignUpSerializer


class SignUp(CreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = SignUpSerializer


# class SignIn(APIView):
#     def post(self, request):
#         username = request.data.get("username", None)
#         password = request.data.get("password", None)

#         if username and password:
#             account = Account.objects.filter(username=username).first()
#             if account and account.check_password(password):
#                 pass

#         return Response(
#             {"detail": "Invalid credentials"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )


# class TokenRetrieve:
#     pass


# class TokenRefresh:
#     pass
