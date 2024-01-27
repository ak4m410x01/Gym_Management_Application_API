from re import match
from django.core.exceptions import ValidationError

def usernameValidator(username: str):
    # Regular expression for usernames
    # username must start with [a-zA-Z_] and contains [a-zA-Z0-9_.]
    regex = r"^[a-zA-Z_][A-Za-z0-9_\.]+$"
    if not match(regex, username):
        raise ValidationError("Invalid username :(")