from re import match
from django.core.exceptions import ValidationError


def twitterLinkValidator(link: str):
    # Regular expression for Twitter links
    regex = r'^https://twitter\.com/[A-Za-z0-9_]{1,15}$'
    if not match(regex, link):
        raise ValidationError("Invalid Twitter link :(")
