from rest_framework import generics

from accounts.models.account import Account, Contact

from accounts.models.admin import Admin
from accounts.serializers.admin import AdminSerializer


class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def perform_destroy(self, instance):
        account = Account.objects.get(id=instance.account.id)
        contact = Contact.objects.get(id=account.contact.id)

        contact.delete()
        account.delete()

        return super().perform_destroy(instance)
