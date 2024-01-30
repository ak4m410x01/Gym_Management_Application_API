from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


def dateOfBirthValidator(date):
    # Check if the date is in the correct format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValidationError("Date of birth must be in the format YYYY-MM-DD.")

    # Check if the date is less than current date minus 5 years
    min_date = datetime.now() - timedelta(days=5 * 365)
    if datetime.strptime(date, "%Y-%m-%d") > min_date:
        raise ValidationError("Date of birth must be at least 5 years ago.")
