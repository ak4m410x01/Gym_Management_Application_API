from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from support.serializers.complaint import ComplaintSerializer
from support.filters.complaint import ComplaintFilter
from support.models.complaint import Complaint
from accounts.permissions.isMember import IsMember
from accounts.permissions.isAdmin import IsAdmin
from authentication.utils.token import JWTToken


class ComplaintListCreate(ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ComplaintFilter

    def get_queryset(self):
        qs = super().get_queryset()

        if not self.request.auth:
            return qs.none()

        token = self.request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        if payload.get("user_role") == "admin":
            return qs
        return qs.filter(member=payload.get("user_id"))

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsMember)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsMember]
        return super().get_permissions()


class ComplaintRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsMember)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsMember]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
