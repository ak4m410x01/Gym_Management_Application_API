from django.urls import path, include
from plans.urls.plan import urlpatterns as plans_urls
from plans.urls.subscription import urlpatterns as subscriptions_urls

app_name = "plans"

urlpatterns = [
    path("", include(plans_urls), name="plans"),
    path("subscriptions/", include(subscriptions_urls), name="subscription"),
]
