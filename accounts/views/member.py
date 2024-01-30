from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.account import Account, Contact
from accounts.models.member import Member
from accounts.serializers.member import MemberSerializer
from accounts.filters.member import MemberFilter


class MemberListCreate(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MemberFilter

    def perform_destroy(self, instance):
        account = Account.objects.get(id=instance.account.id)
        contact = Contact.objects.get(id=account.contact.id)

        contact.delete()
        account.delete()

        return super().perform_destroy(instance)
