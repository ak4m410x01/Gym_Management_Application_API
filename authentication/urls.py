from django.urls import path


from authentication.views.verifyemail import VerifyEmail
from authentication.views.signup import SignUp

from authentication.views.obtain_pair_token import ObtainPairTokenView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView


app_name = "authentication"


urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("signup/verify/", VerifyEmail.as_view(), name="verifyemail"),
    # Token
    path("token/", ObtainPairTokenView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
