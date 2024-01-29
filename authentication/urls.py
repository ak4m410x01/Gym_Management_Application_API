from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view()),
    path("signin/", views.SignIn.as_view()),
    # path("token/", views.TokenRetrieve.as_view()),
    # path("token/refresh/", views.TokenRefresh.as_view()),
]
