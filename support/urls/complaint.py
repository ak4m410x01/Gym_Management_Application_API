from django.urls import path
from support.views.complaint import ComplaintListCreate, ComplaintRetrieveUpdateDestroy

urlpatterns = [
    path("", ComplaintListCreate.as_view(), name="ComplaintListCreate"),
    path(
        "<int:pk>/",
        ComplaintRetrieveUpdateDestroy.as_view(),
        name="ComplaintRetrieveUpdateDestroy",
    ),
]
