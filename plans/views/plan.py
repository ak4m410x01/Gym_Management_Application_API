from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from plans.models.plan import Plan
from plans.serializers.plan import PlanSerializer


class PlanListCreate(ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
