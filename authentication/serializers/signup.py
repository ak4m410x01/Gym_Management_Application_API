from re import match
from rest_framework.serializers import ValidationError

from accounts.serializers.visitor import BaseVisitorSerializer
from accounts.models.account import Account, Contact
from accounts.models.visitor import Visitor


class SignUpSerializer(BaseVisitorSerializer):
    def validate_email(self, email: str) -> str:
        if Account.objects.filter(email=email).exists():
            raise ValidationError("email already exists.")
        return email

    def validate_username(self, username: str) -> str:
        if Account.objects.filter(username=username).exists():
            raise ValidationError("username already exists.")
        return username

    def validate_gender(self, gender: str) -> str:
        regex = r"^[MF]$"
        if not match(regex, gender):
            raise ValidationError("gender must be 'M' or 'F'.")
        return gender

    def create(self, validated_data):
        account_data = validated_data.pop("account", {})
        contact_data = account_data.pop("contact", {})

        contact = Contact.objects.create(**contact_data)
        account = Account.objects.create(contact=contact, **account_data)
        visitor = Visitor.objects.create(account=account, **validated_data)

        return visitor
