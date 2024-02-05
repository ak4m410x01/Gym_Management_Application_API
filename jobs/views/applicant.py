from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from jobs.serializers.applicant import ApplicantSerializer
from jobs.models.applicant import Applicant
from authentication.utils.token import JWTToken


class ApplicantListCreate(ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    lookup_field = "applicant_id"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(job=self.kwargs.get("pk"))

        if not self.request.auth:
            return qs.none()

        token = self.request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        if payload.get("user_role") == "admin":
            return qs

        return qs.filter(applicant__username=payload.get("username"))


class ApplicantRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    lookup_field = "applicant_id"
