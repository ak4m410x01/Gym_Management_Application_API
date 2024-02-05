from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.permissions.isAdmin import IsAdmin
from jobs.serializers.job import JobSerializer
from jobs.models.job import Job


class JobListCreate(ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class JobRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
