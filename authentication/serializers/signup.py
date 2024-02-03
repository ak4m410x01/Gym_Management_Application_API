from re import match
from rest_framework.serializers import ValidationError
from accounts.serializers.visitor import BaseVisitorSerializer
from accounts.models.user import User, Contact
from accounts.models.visitor import Visitor


class SignUpSerializer(BaseVisitorSerializer):
    def validate_email(self, email: str) -> str:
        if User.objects.filter(email=email).exists():
            raise ValidationError("email already exists.")
        return email

    def validate_username(self, username: str) -> str:
        if User.objects.filter(username=username).exists():
            raise ValidationError("username already exists.")
        return username

    def validate_gender(self, gender: str) -> str:
        regex = r"^[MF]$"
        if not match(regex, gender):
            raise ValidationError("gender must be 'M' or 'F'.")
        return gender

    def create(self, validated_data):
        user_data = validated_data.pop("user", {})
        contact_data = user_data.pop("contact", {})

        contact = Contact.objects.create(**contact_data)
        user = User.objects.create(contact=contact, **user_data)
        visitor = Visitor.objects.create(user=user, **validated_data)

        return visitor
