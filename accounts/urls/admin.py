from django.urls import path

from ..views.admin import AdminListCreate, AdminRetrieveUpdateDestroy

urlpatterns = [
    path("", AdminListCreate.as_view()),
    path("<int:pk>/", AdminRetrieveUpdateDestroy.as_view()),
]
