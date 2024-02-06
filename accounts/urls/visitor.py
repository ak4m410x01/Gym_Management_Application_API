from django.urls import path
from accounts.views.visitor import VisitorListCreate, VisitorRetrieveUpdateDestroy

urlpatterns = [
    path("", VisitorListCreate.as_view()),
    path(
        "<int:pk>/",
        VisitorRetrieveUpdateDestroy.as_view(),
        name="VisitorRetrieveUpdateDestroy",
    ),
]
