from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.serializers.member import MemberSerializer
from accounts.permissions.isMember import IsMember
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.noOne import NoOne
from accounts.filters.member import MemberFilter
from accounts.models.user import User, Contact
from accounts.models.member import Member


class MemberListCreate(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MemberFilter

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "POST":
            self.permission_classes = [NoOne]
        return super().get_permissions()


class MemberRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsMember]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsMember)]
        return super().get_permissions()
