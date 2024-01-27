from re import match
from django.core.exceptions import ValidationError


def instagramLinkValidator(link: str):
    # Regular expression for Instagram links
    regex = r'^https://www\.instagram\.com/[A-Za-z0-9_\.]+$'
    if not match(regex, link):
        raise ValidationError("Invalid Instagram link :(")
