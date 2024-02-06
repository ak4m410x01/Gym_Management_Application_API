from django.db import models
from jobs.models.job import Job
from accounts.models.user import User


class Applicant(models.Model):
    STATUS = (
        ("not seen", "not seen"),
        ("seen", "seen"),
        ("refused", "refused"),
        ("accepted", "accepted"),
    )
    status = models.CharField(max_length=8, choices=STATUS, default="not seen")
    applied_at = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(User, models.CASCADE)
    job = models.ForeignKey(Job, models.CASCADE)

    class Meta:
        unique_together = ("applicant", "job")

    def __str__(self) -> str:
        return f"{self.applicant.username}"
