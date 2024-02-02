from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from accounts.models.user import User, Contact
from accounts.models.visitor import Visitor
from accounts.serializers.visitor import VisitorSerializer
from accounts.filters.visitor import VisitorFilter

from accounts.permissions.isDeveloper import IsDeveloper
from accounts.permissions.isVisitor import IsVisitor
from accounts.permissions.isAdmin import IsAdmin


class VisitorListCreate(ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VisitorFilter

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper(), IsAuthenticated())
        elif self.request.method == "POST":
            return (IsDeveloper(),)
        else:
            return ()


class VisitorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

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
            return (IsDeveloper(), IsAuthenticated(), IsVisitor())
        elif self.request.method == "DELETE":
            return (IsDeveloper(), IsAuthenticated(), IsAdmin(), IsVisitor())
        else:
            return ()
