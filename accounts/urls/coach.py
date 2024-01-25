from django.urls import path
from accounts.views.coach import CoachListCreate, CoachMemberRetrieveUpdateDestroy

urlpatterns = [
    path("", CoachListCreate.as_view()),
    path("<int:pk>/", CoachMemberRetrieveUpdateDestroy.as_view()),
]
