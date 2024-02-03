from django.db import models
from django.contrib.auth.models import AbstractUser


class Contact(models.Model):
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.phone)


class User(AbstractUser):
    GENDER = (
        ("m", "male"),
        ("f", "female"),
    )

    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=5000)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField()

    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        unique=True,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
        "password",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
    ]

    class Meta:
        swappable = "AUTH_USER_MODEL"

    def __str__(self) -> str:
        return str(self.username)
