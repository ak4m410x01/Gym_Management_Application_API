from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("auth/", include("authentication.urls")),
]
