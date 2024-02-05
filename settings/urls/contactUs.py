from django.urls import path
from settings.views.contactUs import ContactUsListCreate, ContactUsRetrieveUpdateDestroy

app_name = "settings"

urlpatterns = [
    path("", ContactUsListCreate.as_view(), name="ContactUsListCreate"),
    path(
        "<int:pk>/",
        ContactUsRetrieveUpdateDestroy.as_view(),
        name="ContactUsRetrieveUpdateDestroy",
    ),
]
