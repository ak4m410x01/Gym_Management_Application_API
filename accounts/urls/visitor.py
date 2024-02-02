from django.urls import path

from accounts.views.visitor import VisitorRetrieveUpdateDestroy

urlpatterns = [
    path("<int:pk>/", VisitorRetrieveUpdateDestroy.as_view()),
]
