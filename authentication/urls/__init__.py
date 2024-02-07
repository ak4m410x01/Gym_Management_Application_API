from django.urls import path, include
from authentication.urls.signup import urlpatterns as signup_urls
from authentication.urls.token import urlpatterns as token_urls

app_name = "authentication"

urlpatterns = [
    path("signup/", include(signup_urls), name="signup"),
    path("token/", include(token_urls), name="token"),
]
