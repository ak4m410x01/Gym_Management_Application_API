from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email: str, username: str, password: str, **extra_fields):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("username is required")
        if not password:
            raise ValueError("password is required")

        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)

        email = self.normalize_email(email)
        username = GlobalUserModel.normalize_username(username)

        user = self.model(email=email, username=username, **extra_fields)
        user.password = make_password(password)
        user.save()
        
        return user

    def create_user(self, email: str, username: str, password: str, **extra_fields):
        user = self._create_user(username, email, password, **extra_fields)
        user.is_superuser = False
        return user

    def create_superuser(self, email: str, username: str, password: str, **extra_fields):
        user = self._create_user(username, email, password, **extra_fields)
        user.is_superuser = True
        return user
