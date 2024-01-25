from django.urls import path
from accounts.views.member import MemberListCreate, MemberRetrieveUpdateDestroy

urlpatterns = [
    path("", MemberListCreate.as_view()),
    path("<int:pk>/", MemberRetrieveUpdateDestroy.as_view()),
]
