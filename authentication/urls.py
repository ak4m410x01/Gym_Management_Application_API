from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView


from authentication.views.signup import SignUp
from authentication.views.verifyemail import VerifyEmail
from authentication.views.signin import SignIn

app_name = "authentication"


urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signup/verify/", VerifyEmail.as_view(), name="verifyemail"),
    path("signin/", SignIn.as_view(), name="signin"),
    # Token
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
