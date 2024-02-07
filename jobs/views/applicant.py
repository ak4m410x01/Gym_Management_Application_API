from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from jobs.permissions.isApplicantOwner import IsApplicantOwner
from jobs.serializers.applicant import ApplicantSerializer
from jobs.models.applicant import Applicant
from accounts.permissions.isAdmin import IsAdmin
from authentication.utils.token import JWTToken


class ApplicantListCreate(ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        token = self.request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        qs = super().get_queryset()
        if payload.get("user_role") == "admin":
            return qs
        return qs.filter(applicant__username=payload.get("username"))

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class ApplicantRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsApplicantOwner | IsAdmin)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
