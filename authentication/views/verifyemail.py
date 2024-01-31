import jwt
from decouple import config

from django.urls import reverse

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from accounts.models.visitor import Account
from authentication.serializers.token import EmailVerificationSerializer


class VerifyEmail(GenericAPIView):
    serializer_class = EmailVerificationSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        response = {}

        if not token:
            response["token"] = "Token is missing."
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = jwt.decode(
                jwt=token, key=config("SECRET_KEY"), algorithms=["HS256"]
            )
            username = payload.get("username")

            account = Account.objects.filter(username=username).first()

            if not account:
                response["error"] = "User does not exist."
                return Response(response, status=status.HTTP_404_NOT_FOUND)

            if account.is_verified:
                response["email"] = "Email already verified."
                return Response(response, status=status.HTTP_200_OK)

            account.is_verified = True
            account.save()
            signin_url = f"{'https' if request.is_secure() else 'http'}://{request.get_host()}{reverse('signin')}"
            response["email"] = "Verification is successful."
            response["signin"] = f"Signin now {signin_url}"

            return Response(response, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            response["error"] = "Expired Token."
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.InvalidTokenError:
            response["error"] = "Invalid Token."
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            response["error"] = f"An error occurred: {str(e)}"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
