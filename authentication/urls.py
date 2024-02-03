from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from authentication.views.verifyemail import VerifyEmail
from authentication.views.signup import SignUp
from authentication.views.obtainPairToken import ObtainPairTokenView

app_name = "authentication"

urlpatterns = [
    path("signup/", SignUp.as_view(), name="SignUp"),
    path("signup/verify/", VerifyEmail.as_view(), name="VerifyEmail"),
    # Token
    path("token/", ObtainPairTokenView.as_view(), name="ObtainPairTokenView"),
    path("token/refresh/", TokenRefreshView.as_view(), name="TokenRefreshView"),
    path("token/verify/", TokenVerifyView.as_view(), name="TokenVerifyView"),
]
