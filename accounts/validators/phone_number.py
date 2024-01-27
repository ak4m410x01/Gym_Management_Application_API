from re import match
from django.core.exceptions import ValidationError


def phoneNumberEgyptValidator(phone: str):
    # Regular expression for Egyptian phone numbers
    # Format: +20 followed by 1, then 0, 1, 2, or 5, followed by 8 digits
    regex = r"^\+201[0125]\d{8}$"
    if not match(regex, phone):
        raise ValidationError("Invalid Egyptian phone number.")
