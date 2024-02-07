from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from authentication.views.obtainPairToken import ObtainPairTokenView

urlpatterns = [
    path("", ObtainPairTokenView.as_view(), name="ObtainPairTokenView"),
    path("refresh/", TokenRefreshView.as_view(), name="TokenRefreshView"),
    path("verify/", TokenVerifyView.as_view(), name="TokenVerifyView"),
]
