from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.serializers.admin import AdminSerializer
from accounts.permissions.isDeveloper import IsDeveloper
from accounts.permissions.isAdmin import IsAdmin
from accounts.filters.admin import AdminFilter
from accounts.models.user import User, Contact
from accounts.models.admin import Admin



class AdminListCreate(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdminFilter

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper() or (IsAuthenticated(),),)
        elif self.request.method == "POST":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        else:
            return ()


class AdminRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsAdmin,)

    def perform_destroy(self, instance):
        user = User.objects.get(id=instance.user.id)
        contact = Contact.objects.get(id=user.contact.id)

        contact.delete()
        user.delete()

        return super().perform_destroy(instance)

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper() or (IsAuthenticated(),),)
        elif self.request.method == "PUT":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        elif self.request.method == "DELETE":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        else:
            return ()
