from re import match
from django.core.exceptions import ValidationError


def telegramLinkValidator(link: str):
    # Regular expression for Telegram links
    regex = r"^https://t\.me/[A-Za-z0-9_]{1,}$"
    if not match(regex, link):
        raise ValidationError("Invalid Telegram link :(")
