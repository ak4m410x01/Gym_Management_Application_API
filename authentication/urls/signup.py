from django.urls import path
from authentication.views.verifyemail import VerifyEmail
from authentication.views.signup import SignUp

urlpatterns = [
    path("", SignUp.as_view(), name="SignUp"),
    path("verify/", VerifyEmail.as_view(), name="VerifyEmail"),
]
