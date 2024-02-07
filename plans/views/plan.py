from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from accounts.permissions.isAdmin import IsAdmin
from plans.serializers.plan import PlanSerializer
from plans.filters.plan import PlanFilter
from plans.models.plan import Plan


class PlanListCreate(ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlanFilter

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class PlanRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
