from rest_framework import generics
from accounts.models.visitor import Visitor
from accounts.serializers.visitor import VisitorSerializer


class VisitorList(generics.ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
