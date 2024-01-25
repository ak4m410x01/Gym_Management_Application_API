from django.urls import path
from accounts.views.admin import AdminListCreate, AdminRetrieveUpdateDestroy

urlpatterns = [
    path("", AdminListCreate.as_view()),
    path("<int:pk>/", AdminRetrieveUpdateDestroy.as_view()),
]
