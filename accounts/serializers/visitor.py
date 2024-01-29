from re import match
from rest_framework import serializers

from accounts.models.visitor import Visitor
from accounts.models.account import Account, Contact


class BaseVisitorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        source="account.email",
    )

    username = serializers.CharField(
        source="account.username",
    )

    password = serializers.CharField(
        source="account.password",
        write_only=True,
    )

    first_name = serializers.CharField(
        source="account.first_name",
    )

    last_name = serializers.CharField(
        source="account.last_name",
    )

    gender = serializers.CharField(
        source="account.gender",
    )

    date_of_birth = serializers.DateField(
        source="account.date_of_birth",
    )

    city = serializers.CharField(
        source="account.city",
        required=False,
    )

    address = serializers.CharField(
        source="account.address",
        required=False,
    )

    phone = serializers.CharField(
        source="account.contact.phone",
        required=False,
    )

    whatsapp = serializers.CharField(
        source="account.contact.whatsapp",
        required=False,
    )

    telegram = serializers.CharField(
        source="account.contact.telegram",
        required=False,
    )

    facebook = serializers.CharField(
        source="account.contact.facebook",
        required=False,
    )

    instagram = serializers.CharField(
        source="account.contact.instagram",
        required=False,
    )

    twitter = serializers.CharField(
        source="account.contact.twitter",
        required=False,
    )

    first_login = serializers.DateTimeField(
        source="account.first_login",
        required=False,
        read_only=True,
    )

    last_login = serializers.DateTimeField(
        source="account.last_login",
        required=False,
        read_only=True,
    )

    joined_at = serializers.DateTimeField(
        source="account.joined_at",
        required=False,
        read_only=True,
    )

    class Meta:
        model = Visitor
        ordering = (id,)
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
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


class VisitorSerializer(BaseVisitorSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get("request") and self.context["request"].method == "PUT":
            for field_name in (
                "email",
                "username",
                "password",
                "first_name",
                "last_name",
                "gender",
                "date_of_birth",
            ):
                self.fields[field_name].required = False

    def validate_username(self, username: str) -> str:
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already exists.")
        return username

    def validate_email(self, email: str) -> str:
        if Account.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists.")
        return email

    def validate_gender(self, gender: str) -> str:
        regex = r"^[MF]$"
        if not match(regex, gender):
            raise serializers.ValidationError("gender must be 'M' or 'F'.")
        return gender

    def update(self, instance, validated_data):
        # Contact Model
        contact_data = validated_data.pop("contact", {})
        for key, value in contact_data.items():
            setattr(instance.account.contact, key, value)
        instance.account.contact.save()

        # Account Model
        account_data = validated_data.pop("account", {})
        for key, value in account_data.items():
            setattr(instance.account, key, value)
        instance.account.save()

        # Visitor Model
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
