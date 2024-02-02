from rest_framework.generics import RetrieveUpdateDestroyAPIView

from accounts.models.visitor import Visitor
from accounts.models.user import User, Contact
from accounts.serializers.visitor import VisitorSerializer
from accounts.permissions.isVisitor import IsVisitor


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
