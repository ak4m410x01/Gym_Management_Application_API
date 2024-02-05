from django.urls import path
from support.views.vacation import VacationListCreate, VacationRetrieveUpdateDestroy

urlpatterns = [
    path("", VacationListCreate.as_view(), name="VacationListCreate"),
    path(
        "<int:pk>/",
        VacationRetrieveUpdateDestroy.as_view(),
        name="VacationRetrieveUpdateDestroy",
    ),
]
