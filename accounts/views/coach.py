from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.user import User, Contact
from accounts.models.coach import Coach
from accounts.serializers.coach import CoachSerializer
from accounts.filters.coach import CoachFilter
from accounts.permissions.isAdmin import IsAdmin

from accounts.permissions.isDeveloper import IsDeveloper
from accounts.permissions.isCoach import IsCoach
from accounts.permissions.isAdmin import IsAdmin


class CoachListCreate(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CoachFilter

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper(), IsAuthenticated())
        elif self.request.method == "POST":
            return (IsDeveloper(), IsAuthenticated(), IsAdmin())
        else:
            return ()


class CoachMemberRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = (IsCoach,)

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper(), IsAuthenticated())
        elif self.request.method == "PUT":
            return (IsDeveloper(), IsAuthenticated(), IsCoach())
        elif self.request.method == "DELETE":
            return (IsDeveloper(), IsAuthenticated(), IsAdmin())
        else:
            return ()
