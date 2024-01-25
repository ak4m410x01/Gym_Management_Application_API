from rest_framework import generics
from accounts.models.coach import Coach
from accounts.serializers.coach import CoachSerializer


class CoachListCreate(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class CoachMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
