from django.db import models
from .account import Account


class Member(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.account.username)
