from django.db import models
from plans.models.subscription import Subscription


class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=20_000, blank=True, null=True)
    eat_at = models.TimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    subscription = models.OneToOneField(Subscription, models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
