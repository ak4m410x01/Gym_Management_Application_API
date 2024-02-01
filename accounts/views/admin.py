from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.user import User, Contact
from accounts.models.admin import Admin
from accounts.serializers.admin import AdminSerializer
from accounts.filters.admin import AdminFilter


class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdminFilter


class AdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)
