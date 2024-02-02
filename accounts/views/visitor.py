from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from accounts.models.visitor import Visitor
from accounts.models.user import User, Contact
from accounts.serializers.visitor import VisitorSerializer
from accounts.filters.visitor import VisitorFilter
from accounts.permissions.isVisitor import IsVisitor


class VisitorList(ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VisitorFilter


class VisitorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = (IsVisitor,)

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsAuthenticated,)
        return super().get_permissions()
