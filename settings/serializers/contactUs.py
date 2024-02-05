from rest_framework import serializers
from settings.models.contactUs import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:settings:ContactUsRetrieveUpdateDestroy", lookup_field="pk"
    )

    class Meta:
        model = ContactUs
        fields = [
            "url",
            "country",
            "city",
            "address",
            "email",
            "phone",
            "whatsapp",
            "telegram",
            "facebook",
            "instagram",
            "twitter",
        ]
