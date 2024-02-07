import jwt
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from authentication.utils.token import JWTToken
from accounts.models.user import User


class VerifyEmail(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")

        if not token:
            return Response(
                {"token": "Token is missing."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            payload = JWTToken.get_payload(token)
            username = payload.get("username")
            user = User.objects.filter(username=username).first()

            if not user:
                return Response(
                    {"user": "User does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            if user.is_verified:
                return Response(
                    {"email": "Email already verified."},
                    status=status.HTTP_200_OK,
                )

            user.is_verified = True
            user.save()
            signin_url = (
                f"{reverse('api:authentication:ObtainPairTokenView',request=request)}"
            )

            return Response(
                {
                    "email": "Verification is successful.",
                    "signin": f"Signin now {signin_url}",
                },
                status=status.HTTP_200_OK,
            )

        except jwt.ExpiredSignatureError:
            return Response(
                {"token": "Expired Token."}, status=status.HTTP_401_UNAUTHORIZED
            )

        except jwt.InvalidTokenError:
            return Response(
                {"token": "Invalid Token."}, status=status.HTTP_401_UNAUTHORIZED
            )

        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
