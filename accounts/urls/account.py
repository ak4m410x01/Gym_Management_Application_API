from django.urls import path

from accounts.views.account import AccountListAPIView

urlpatterns = [
    path("", AccountListAPIView.as_view()),
]
