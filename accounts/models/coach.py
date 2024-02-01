from django.db import models

from accounts.models.user import User


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self) -> str:
        return str(self.user.username)


class Salary(models.Model):
    salary = models.IntegerField(default=0)
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE, unique=True)

    def __str__(self) -> str:
        return str(self.coach.user.username)
