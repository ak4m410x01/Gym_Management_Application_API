from django.urls import path

from authentication.views.signup import SignUp
from authentication.views.verifyemail import VerifyEmail
from authentication.views.signin import SignIn

app_name = "authentication"

urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signup/verify/", VerifyEmail.as_view(), name="verifyemail"),
    path("signin/", SignIn.as_view(), name="signin"),
]
