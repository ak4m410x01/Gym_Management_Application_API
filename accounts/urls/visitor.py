from django.urls import path

from ..views.visitor import VisitorListCreate, VisitorRetrieveUpdateDestroy

urlpatterns = [
    path("", VisitorListCreate.as_view()),
    path("<int:pk>/", VisitorRetrieveUpdateDestroy.as_view()),
]
