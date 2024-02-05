from jwt import decode
from decouple import config
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from support.serializers.complaint import ComplaintSerializer
from support.filters.complaint import ComplaintFilter
from support.models.complaint import Complaint


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
        payload = decode(token, key=config("JWT_SECRET_KEY"), algorithms=["HS256"])

        if payload.get("user_role") == "admin":
            return qs
        return qs.filter(member=payload.get("user_id"))


class ComplaintRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
