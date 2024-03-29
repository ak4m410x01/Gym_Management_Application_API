from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from authentication.serializers.signup import SignUpSerializer
from authentication.tasks.sendMail import send_mail


class SignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            visitor = serializer.save()

            # Generate Email Components
            token = RefreshToken.for_user(visitor.user)
            token["role"] = "visitor"

            verify_url = f"{reverse('api:authentication:VerifyEmail',request=request)}?token={token}"
            email = {
                "send_to": visitor.user.email,
                "subject": "GYM Sign Up Verification",
                "body": f"Dear, {visitor.user.username}... !!\n\n\nUse the link below to verify your email: \n\n{verify_url}",
            }

            # Send Email
            send_mail.delay(email.get("subject"), email.get("body"), [email.get("to")])

            return Response(
                {
                    "detail": f"Thank you for signing up :) Verify Your Email Address !!",
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
