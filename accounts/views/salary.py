from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.salary import CoachSalarySerializer
from accounts.permissions.isDeveloper import IsDeveloper
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isCoach import IsCoach
from accounts.models.salary import CoachSalary


class CoachSalaryListCreate(ListCreateAPIView):
    queryset = CoachSalary.objects.all()
    serializer_class = CoachSalarySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        elif self.request.method == "POST":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        else:
            return ()


class CoachSalaryRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CoachSalary.objects.all()
    serializer_class = CoachSalarySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsDeveloper() or (IsAuthenticated() and (IsAdmin(), IsCoach()),),)
        elif self.request.method == "PUT":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        elif self.request.method == "DELETE":
            return (IsDeveloper() or (IsAuthenticated() and IsAdmin(),),)
        else:
            return ()
