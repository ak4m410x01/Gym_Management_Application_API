from django.db import models
from .account import Account


class Coach(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, unique=True)

    def __str__(self) -> str:
        return str(self.account.username)


class Salary(models.Model):
    salary = models.IntegerField(default=0)
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE, unique=True)

    def __str__(self) -> str:
        return str(self.coach.account.username)
