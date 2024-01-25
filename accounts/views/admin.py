from rest_framework import generics
from accounts.models.admin import Admin
from accounts.serializers.admin import AdminSerializer


class AdminRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
