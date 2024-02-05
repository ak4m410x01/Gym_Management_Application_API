from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from jobs.serializers.job import JobSerializer
from jobs.models.job import Job


class JobListCreate(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
