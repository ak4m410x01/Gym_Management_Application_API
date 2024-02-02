from django.urls import path

from accounts.views.coach import CoachListCreate, CoachRetrieveUpdateDestroy
from accounts.views.salary import (
    CoachSalaryListCreate,
    CoachSalaryRetrieveUpdateDestroy,
)

urlpatterns = [
    path("", CoachListCreate.as_view(), name="CoachListCreate"),
    path(
        "<int:pk>/",
        CoachRetrieveUpdateDestroy.as_view(),
        name="CoachRetrieveUpdateDestroy",
    ),
    # Salary
    path("salaries/", CoachSalaryListCreate.as_view(), name="CoachSalaryListCreate"),
    path(
        "salaries/<int:pk>/",
        CoachSalaryRetrieveUpdateDestroy.as_view(),
        name="CoachSalaryRetrieveUpdateDestroy",
    ),
]
