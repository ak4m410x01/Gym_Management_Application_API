from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.account import Account, Contact
from accounts.models.coach import Coach
from accounts.serializers.coach import CoachSerializer
from accounts.filters.coach import CoachFilter


class CoachListCreate(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CoachFilter



class CoachMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    
    def perform_destroy(self, instance):
        account = Account.objects.get(id=instance.account.id)
        contact = Contact.objects.get(id=account.contact.id)

        contact.delete()
        account.delete()

        return super().perform_destroy(instance)
