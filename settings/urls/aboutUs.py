from django.urls import path
from settings.views.aboutUs import AboutUsListCreate, AboutUsRetrieveUpdateDestroy


urlpatterns = [
    path("", AboutUsListCreate.as_view(), name="AboutUsListCreate"),
    path(
        "<int:pk>/",
        AboutUsRetrieveUpdateDestroy.as_view(),
        name="AboutUsRetrieveUpdateDestroy",
    ),
]
