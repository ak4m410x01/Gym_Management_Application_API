from django.db import models
from accounts.models.account import Account


class Visitor(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.account.username)
