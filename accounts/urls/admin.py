from django.urls import path
from accounts.views.admin import AdminRetrieveUpdate

urlpatterns = [
    path("<int:pk>/", AdminRetrieveUpdate.as_view()),
]
