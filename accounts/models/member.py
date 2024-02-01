from django.db import models

from accounts.models.user import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self) -> str:
        return str(self.user.username)
