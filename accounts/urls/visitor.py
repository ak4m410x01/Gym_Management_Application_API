from django.urls import path
from accounts.views.visitor import VisitorList, VisitorRetrieveUpdateDestroy

urlpatterns = [
    path("", VisitorList.as_view()),
    path("<int:pk>/", VisitorRetrieveUpdateDestroy.as_view()),
]
