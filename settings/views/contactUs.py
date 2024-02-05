from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from settings.models.contactUs import ContactUs
from settings.serializers.contactUs import ContactUsSerializer


class ContactUsListCreate(ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ContactUsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
