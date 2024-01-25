from django.urls import path
from accounts.views.member import MemberList, MemberRetrieveUpdateDestroy

urlpatterns = [
    path("", MemberList.as_view()),
    path("<int:pk>/", MemberRetrieveUpdateDestroy.as_view()),
]
