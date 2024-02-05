from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.serializers.coach import CoachSerializer
from accounts.permissions.isCoach import IsCoach
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.noOne import NoOne
from accounts.filters.coach import CoachFilter
from accounts.models.user import User, Contact
from accounts.models.coach import Coach


class CoachListCreate(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CoachFilter

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         self.permission_classes = [IsAuthenticated]
    #     elif self.request.method == "POST":
    #         self.permission_classes = [NoOne]
    #     return super().get_permissions()


class CoachRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated()]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated() & IsCoach()]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated() & IsAdmin()]
        return super().get_permissions()
