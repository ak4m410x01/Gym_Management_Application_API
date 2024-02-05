from rest_framework import serializers
from settings.models.aboutUs import AboutUs
from settings.serializers.contactUs import ContactUsSerializer


class AboutUsSerializer(serializers.ModelSerializer):
    contact_us = ContactUsSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = [
            "id",
            "the_face_of_your_business",
            "who_are_serve",
            "our_mission",
            "our_goals",
            "contact_us",
        ]
