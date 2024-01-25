from rest_framework import serializers
from accounts.models.coach import Coach


class CoachSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="account.email")
    username = serializers.CharField(source="account.username")
    first_name = serializers.CharField(source="account.first_name")
    last_name = serializers.CharField(source="account.last_name")
    gender = serializers.CharField(source="account.gender")
    date_of_birth = serializers.DateField(source="account.date_of_birth")
    country = serializers.CharField(source="account.country")
    city = serializers.CharField(source="account.city")
    address = serializers.CharField(source="account.address")
    first_login = serializers.DateTimeField(source="account.first_login")
    last_login = serializers.DateTimeField(source="account.last_login")
    joined_at = serializers.DateTimeField(source="account.joined_at")
    phone = serializers.CharField(source="account.contact.phone")
    whatsapp = serializers.CharField(source="account.contact.whatsapp")
    telegram = serializers.CharField(source="account.contact.telegram")
    facebook = serializers.CharField(source="account.contact.facebook")
    instagram = serializers.CharField(source="account.contact.instagram")
    twitter = serializers.CharField(source="account.contact.twitter")

    class Meta:
        model = Coach
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "salary",
            "country",
            "city",
            "address",
            "phone",
            "whatsapp",
            "telegram",
            "facebook",
            "instagram",
            "twitter",
            "first_login",
            "last_login",
            "joined_at",
        ]
