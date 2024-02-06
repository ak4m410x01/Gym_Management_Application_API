from django.db import models


class Plan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=20_000, blank=True, null=True)
    price = models.IntegerField(default=0)
    classes = models.IntegerField(default=0)
    max_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"
