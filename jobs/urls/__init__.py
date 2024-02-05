from django.urls import path, include
from jobs.urls.job import urlpatterns as job_urls
from jobs.urls.applicant import urlpatterns as applicant_urls

app_name = "jobs"

urlpatterns = [
    path("", include(job_urls), name="jobs"),
    path("applicants/", include(applicant_urls), name="applicants"),
]
