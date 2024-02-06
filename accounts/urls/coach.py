from django.urls import path
from accounts.views.coach import CoachListCreate, CoachRetrieveUpdateDestroy

urlpatterns = [
    path("", CoachListCreate.as_view(), name="CoachListCreate"),
    path(
        "<int:pk>/",
        CoachRetrieveUpdateDestroy.as_view(),
        name="CoachRetrieveUpdateDestroy",
    ),
]
