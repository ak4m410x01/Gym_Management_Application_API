from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from support.models.vacation import Vacation
from support.serializers.vacation import VacationSerializer


class VacationListCreate(ListCreateAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer


class VacationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
