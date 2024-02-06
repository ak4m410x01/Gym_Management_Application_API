from django.urls import path, include
from plans.urls.plan import urlpatterns as plans_urls

app_name = "plans"

urlpatterns = [
    path("", include(plans_urls), name="plans"),
]
