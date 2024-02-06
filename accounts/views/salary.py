from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.salary import CoachSalarySerializer
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isCoach import IsCoach
from accounts.models.salary import CoachSalary
from authentication.utils.token import JWTToken


class CoachSalaryListCreate(ListCreateAPIView):
    queryset = CoachSalary.objects.all()
    serializer_class = CoachSalarySerializer

    def get_queryset(self):
        qs = super().get_queryset()

        token = self.request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        if payload.get("user_role") == "admin":
            return qs
        elif payload.get("username") == self.request.user.username:
            return qs.filter(coach__user__username=self.request.user.username)
        return qs.none()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsCoach | IsAdmin)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class CoachSalaryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CoachSalary.objects.all()
    serializer_class = CoachSalarySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsCoach | IsAdmin)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
