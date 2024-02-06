from django.urls import path
from accounts.views.salary import (
    CoachSalaryListCreate,
    CoachSalaryRetrieveUpdateDestroy,
)

urlpatterns = [
    path(
        "",
        CoachSalaryListCreate.as_view(),
        name="CoachSalaryListCreate",
    ),
    path(
        "<int:pk>/",
        CoachSalaryRetrieveUpdateDestroy.as_view(),
        name="CoachSalaryRetrieveUpdateDestroy",
    ),
]
