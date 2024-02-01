from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission

from accounts.models.usermanager import UserManager

from accounts.validators.phone_number import phoneNumberEgyptValidator
from accounts.validators.whatsappLink import whastappLinkEgyptValidator
from accounts.validators.telegramLink import telegramLinkValidator
from accounts.validators.facebookLink import facebookLinkValidator
from accounts.validators.instagramLink import instagramLinkValidator
from accounts.validators.twitterLink import twitterLinkValidator

class Contact(models.Model):
    phone = models.CharField(max_length=13, blank=True, null=True, validators=[phoneNumberEgyptValidator])
    whatsapp = models.CharField(max_length=50, blank=True, null=True, validators=[whastappLinkEgyptValidator])
    telegram = models.CharField(max_length=50, blank=True, null=True, validators=[telegramLinkValidator])
    facebook = models.CharField(max_length=50, blank=True, null=True, validators=[facebookLinkValidator])
    instagram = models.CharField(max_length=50, blank=True, null=True, validators=[instagramLinkValidator])
    twitter = models.CharField(max_length=50, blank=True, null=True, validators=[twitterLinkValidator])

    def __str__(self) -> str:
        return str(self.phone)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (('m','male'), ('f','female'))
    
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=5000)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField()

    city = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    last_login = models.DateTimeField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, unique=True, null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password", "first_name", "last_name", "gender", "date_of_birth"]

    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="account_user_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="account_user_set",
        related_query_name="user",
    )

    class Meta:
        swappable = "AUTH_USER_MODEL"

    def __str__(self) -> str:
        return str(self.username)
