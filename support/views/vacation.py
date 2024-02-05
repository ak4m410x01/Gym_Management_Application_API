from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from support.serializers.vacation import VacationSerializer
from support.filters.vacation import VacationFilter
from support.models.vacation import Vacation

from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isCoach import IsCoach

from jwt import decode
from decouple import config


class VacationListCreate(ListCreateAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VacationFilter

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.auth:
            return qs.none()

        token = self.request.auth.token.decode()
        payload = decode(token, key=config("JWT_SECRET_KEY"), algorithms=["HS256"])

        if payload.get("user_role") == "admin":
            return qs
        return qs.filter(coach=payload.get("user_id"))

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsCoach)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsCoach]
        return super().get_permissions()


class VacationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsCoach)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsCoach]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
