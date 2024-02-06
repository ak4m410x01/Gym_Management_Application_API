from django.db import models
from accounts.models.coach import Coach


class CoachSalary(models.Model):
    salary = models.IntegerField(default=0)
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE, unique=True)

    class Meta:
        unique_together = ("coach", "salary")

    def __str__(self) -> str:
        return str(self.coach.user.username)
