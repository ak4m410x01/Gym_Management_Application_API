from django.urls import path
from jobs.views.job import JobListCreate, JobRetrieveUpdateDestroy

urlpatterns = [
    path("", JobListCreate.as_view(), name="JobListCreate"),
    path(
        "<int:pk>/", JobRetrieveUpdateDestroy.as_view(), name="JobRetrieveUpdateDestroy"
    ),
]
