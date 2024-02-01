from re import match
from rest_framework import serializers

from accounts.models.member import Member
from accounts.models.user import User, Contact


class BaseMemberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(source="user.password", write_only=True)

    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    gender = serializers.CharField(source="user.gender")
    date_of_birth = serializers.DateField(source="user.date_of_birth")

    city = serializers.CharField(source="user.city", required=False)
    address = serializers.CharField(source="user.address", required=False)

    phone = serializers.CharField(source="user.contact.phone", required=False)
    whatsapp = serializers.CharField(source="user.contact.whatsapp", required=False)
    telegram = serializers.CharField(source="user.contact.telegram", required=False)
    facebook = serializers.CharField(source="user.contact.facebook", required=False)
    instagram = serializers.CharField(source="user.contact.instagram", required=False)
    twitter = serializers.CharField(source="user.contact.twitter", required=False)

    is_active = serializers.BooleanField(source="user.is_active", required=False, read_only=True)
    is_staff = serializers.BooleanField(source="user.is_staff", required=False, read_only=True)
    is_superuser = serializers.BooleanField(source="user.is_superuser", required=False, read_only=True)
    is_verified = serializers.BooleanField(source="user.is_verified", required=False, read_only=True)

    last_login = serializers.DateTimeField(source="user.last_login", required=False, read_only=True)
    date_joined = serializers.DateTimeField(source="user.joined_at", required=False, read_only=True)

    class Meta:
        model = Member
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
            "is_active",
            "is_staff",
            "is_superuser",
            "is_verified",
            "last_login",
            "date_joined",
        ]


class MemberSerializer(BaseMemberSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get("request") and self.context["request"].method == "PUT":
            for field_name in ("email", "username", "password", "first_name", "last_name", "gender", "date_of_birth"):
                self.fields[field_name].required = False

    def validate_username(self, username: str) -> str:
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(f"username already exists.")
        return username

    def validate_email(self, email: str) -> str:
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(f"email already exists.")
        return email

    def validate_gender(self, gender: str) -> str:
        regex = r"^[MF]$"
        if not match(regex, gender):
            raise serializers.ValidationError(f"gender must be 'M' or 'F'.")
        return gender

    def create(self, validated_data):
        user_data = validated_data.pop("user", {})
        contact_data = user_data.pop("contact", {})

        contact = Contact.objects.create(**contact_data)
        user = User.objects.create(contact=contact, **user_data)
        member = Member.objects.create(user=user, **validated_data)

        return member

    def update(self, instance, validated_data):
        # Contact Model
        contact_data = validated_data.pop("contact", {})
        for key, value in contact_data.items():
            setattr(instance.user.contact, key, value)
        instance.user.contact.save()

        # User Model
        user_data = validated_data.pop("user", {})
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()

        # Member Model
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
