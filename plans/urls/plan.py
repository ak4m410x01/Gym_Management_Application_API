from django.urls import path
from plans.views.plan import PlanListCreate, PlanRetrieveUpdateDestroy

urlpatterns = [
    path("", PlanListCreate.as_view(), name="PlanListCreate"),
    path(
        "<int:pk>/",
        PlanRetrieveUpdateDestroy.as_view(),
        name="PlanRetrieveUpdateDestroy",
    ),
]
