from django.urls import path, include
from support.urls.complaint import urlpatterns as complaint_urls
from support.urls.vacation import urlpatterns as vacation_urls

app_name = "support"

urlpatterns = [
    path("complaints/", include(complaint_urls), name="complaints"),
    path("vacations/", include(vacation_urls), name="vacations"),
]
