from re import match
from django.core.exceptions import ValidationError


def whastappLinkEgyptValidator(phone: str):
    # Regular expression for WhatsApp links with Egyptian phone numbers
    regex = r"^https://wa\.me/20[0125]\d{8}$"
    if not match(regex, phone):
        raise ValidationError("Invalid WhatsApp link for an Egyptian phone number :(")
