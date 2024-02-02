from django.urls import path

from accounts.views.member import MemberList, MemberRetrieveUpdate

urlpatterns = [
    path("", MemberList.as_view()),
    path("<int:pk>/", MemberRetrieveUpdate.as_view()),
]
