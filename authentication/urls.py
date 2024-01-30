from django.urls import path

from authentication.views.signup import SignUp
from authentication.views.signin import SignIn

from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


urlpatterns = [
    path("signup/", SignUp.as_view()),
    path("signin/", SignIn.as_view()),
    
    path("token/", TokenObtainSlidingView.as_view()),
    path("token/refresh/", TokenRefreshSlidingView.as_view()),
]
