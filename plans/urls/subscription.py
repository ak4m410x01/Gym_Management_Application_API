from django.urls import path
from plans.views.subscription import (
    SubscriptionListCreate,
    SubscriptionRetrieveUpdateDestroy,
)

urlpatterns = [
    path("", SubscriptionListCreate.as_view(), name="SubscriptionListCreate"),
    path(
        "<int:pk>/",
        SubscriptionRetrieveUpdateDestroy.as_view(),
        name="SubscriptionRetrieveUpdateDestroy",
    ),
]
