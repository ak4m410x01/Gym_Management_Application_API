from re import match
from django.core.exceptions import ValidationError


def genderValidator(gender: str):
    regex = r"^[mf]$"
    if match(regex, gender):
        raise ValidationError("Gender should be either 'm' or 'f'.")
