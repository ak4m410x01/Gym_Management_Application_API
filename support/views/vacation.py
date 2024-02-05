from jwt import decode
from decouple import config
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from support.serializers.vacation import VacationSerializer
from support.filters.vacation import VacationFilter
from support.models.vacation import Vacation


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


class VacationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
