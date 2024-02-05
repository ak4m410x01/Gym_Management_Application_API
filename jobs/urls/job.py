from django.urls import path
from jobs.views.job import JobListCreate, JobRetrieveUpdateDestroy
from jobs.views.applicant import ApplicantListCreate, ApplicantRetrieveUpdateDestroy


urlpatterns = [
    # Jobs
    path(
        "",
        JobListCreate.as_view(),
        name="JobListCreate",
    ),
    path(
        "<int:pk>/",
        JobRetrieveUpdateDestroy.as_view(),
        name="JobRetrieveUpdateDestroy",
    ),
    # ----------------------------------------
    # Job Applicants
    path(
        "<int:pk>/applicants/",
        ApplicantListCreate.as_view(),
        name="ApplicantListCreate",
    ),
    path(
        "<int:job_id>/applicants/<int:applicant_id>/",
        ApplicantRetrieveUpdateDestroy.as_view(),
        name="ApplicantRetrieveUpdateDestroy",
    ),
]
