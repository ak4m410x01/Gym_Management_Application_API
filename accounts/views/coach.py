from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.user import User, Contact
from accounts.models.coach import Coach
from accounts.serializers.coach import CoachSerializer
from accounts.filters.coach import CoachFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isCoach import IsCoach


class CoachListCreate(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CoachFilter
    permission_classes = (IsAdmin,)


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
        if self.request.method == "DELETE":
            return (IsAdmin,)
        return super().get_permissions()
