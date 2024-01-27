from re import match
from django.core.exceptions import ValidationError


def facebookLinkValidator(link: str):
    # Regular expression for Facebook links
    regex = r'^https://www\.facebook\.com/[A-Za-z0-9.]+$'
    if not match(regex, link):
        raise ValidationError("Invalid Facebook link :(")
