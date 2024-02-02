from django.urls import path

from accounts.views.member import MemberListCreate, MemberRetrieveUpdate

urlpatterns = [
    path("", MemberListCreate.as_view()),
    path("<int:pk>/", MemberRetrieveUpdate.as_view()),
]
