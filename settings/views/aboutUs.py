from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from settings.models.aboutUs import AboutUs
from settings.serializers.aboutUs import AboutUsSerializer


class AboutUsListCreate(ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class AboutUsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
