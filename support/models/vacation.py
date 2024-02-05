from django.db import models
from accounts.models.coach import Coach


class Vacation(models.Model):
    STATUS = (
        ("not seen", "not seen"),
        ("seen", "seen"),
        ("refused", "refused"),
        ("accepted", "accepted"),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10_000, blank=True, null=True)
    reason = models.TextField(max_length=10_000, blank=True, null=True)
    start_at = models.DateField()
    end_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUS, default="not seen")

    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.coach.user.username}"
