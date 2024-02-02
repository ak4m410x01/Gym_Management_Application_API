from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.user import User, Contact
from accounts.models.member import Member
from accounts.serializers.member import MemberSerializer
from accounts.filters.member import MemberFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isMember import IsMember


class MemberList(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAdmin)


class MemberRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MemberFilter
    permission_classes = (IsMember,)

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)
