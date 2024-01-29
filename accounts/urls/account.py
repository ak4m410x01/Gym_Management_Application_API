from django.urls import path

from ..views.account import AccountListAPIView

urlpatterns = [
    path("", AccountListAPIView.as_view()),
]
