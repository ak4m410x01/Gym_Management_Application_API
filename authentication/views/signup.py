from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from authentication.serializers.signup import SignUpSerializer


class SignUp(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            visitor = serializer.save()

            # Generate Email Components
            token = RefreshToken.for_user(visitor)
            token["username"] = visitor.account.username

            if "user_id" in token:
                del token["user_id"]

            verify_url = f"http://{get_current_site(request).domain}{reverse('verifyemail')}?token={token}"
            email = {
                "to": visitor.account.email,
                "subject": "GYM Sign Up Verification",
                "body": f"Dear, {visitor.account.username}... !!\n\n\nUse the link below to verify your email: \n\n{verify_url}",
            }

            # Send Email
            send_mail(
                from_email=EMAIL_HOST_USER,
                recipient_list=[email.get("to")],
                subject=email.get("subject"),
                message=email.get("body"),
            )

            response = {
                "detail": f"Thank you for signing up :) Verify Your Email Address !!"
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
