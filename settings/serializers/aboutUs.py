from rest_framework import serializers
from settings.models.aboutUs import AboutUs
from settings.serializers.contactUs import ContactUsSerializer

class AboutUsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:settings:AboutUsRetrieveUpdateDestroy", lookup_field="pk"
    )
    contact = ContactUsSerializer()

    class Meta:
        model = AboutUs
        fields = [
            "url",
            "the_face_of_your_business",
            "who_are_serve",
            "our_mission",
            "our_goals",
            "contact",
        ]
