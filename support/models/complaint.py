from django.db import models
from accounts.models.member import Member


class Complaint(models.Model):
    SEND_TO = (
        ("admin", "admin"),
        ("coach", "coach"),
    )
    STATUS = (
        ("seen", "seen"),
        ("not seen", "not seen"),
    )
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    description = models.TextField(max_length=10_000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    send_to = models.CharField(max_length=5, choices=SEND_TO, default="coach")
    status = models.CharField(max_length=8, choices=STATUS, default="not seen")

    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.member.user.username}"
