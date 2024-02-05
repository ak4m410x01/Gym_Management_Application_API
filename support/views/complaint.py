from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from support.models.complaint import Complaint
from support.serializers.complaint import ComplaintSerializer


class ComplaintListCreate(ListCreateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


class ComplaintRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
