from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.user import User, Contact
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
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)
