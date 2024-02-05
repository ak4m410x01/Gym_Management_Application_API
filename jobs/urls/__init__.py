from django.urls import path, include
from jobs.urls.job import urlpatterns as job_urls

app_name = "jobs"

urlpatterns = [
    path("", include(job_urls), name="jobs"),
]
