from django.urls import path
from accounts.views.user import UserListAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="UserListAPIView"),
]
