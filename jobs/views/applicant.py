from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from jobs.serializers.applicant import ApplicantSerializer
from jobs.models.applicant import Applicant


class ApplicantListCreate(ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class ApplicantRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
