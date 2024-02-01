import jwt
from decouple import config

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from accounts.models.user import User


class VerifyEmail(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        response = {}

        if not token:
            response["token"] = "Token is missing."
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = jwt.decode(
                jwt=token,
                key=config("JWT_SECRET_KEY"),
                algorithms=["HS256"],
            )

            username = payload.get("username")

            user = User.objects.filter(username=username).first()

            if not user:
                response["error"] = "User does not exist."
                return Response(response, status=status.HTTP_404_NOT_FOUND)

            if user.is_verified:
                response["email"] = "Email already verified."
                return Response(response, status=status.HTTP_200_OK)

            user.is_verified = True
            user.save()
            signin_url = f"{'https' if request.is_secure() else 'http'}://{request.get_host()}/api/auth/signin/"
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
