from django.urls import path
from jobs.views.applicant import ApplicantListCreate, ApplicantRetrieveUpdateDestroy


urlpatterns = [
    path("", ApplicantListCreate.as_view(), name="ApplicantListCreate"),
    path(
        "<int:pk>/",
        ApplicantRetrieveUpdateDestroy.as_view(),
        name="ApplicantRetrieveUpdateDestroy",
    ),
]
