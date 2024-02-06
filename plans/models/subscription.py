from django.db import models
from accounts.models.coach import Coach
from accounts.models.member import Member
from plans.models.plan import Plan


class Subscription(models.Model):
    title = models.CharField(max_length=100)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    coach = models.ForeignKey(Coach, models.CASCADE)
    member = models.ForeignKey(Member, models.CASCADE)
    plan = models.ForeignKey(Plan, models.CASCADE)

    class Meta:
        unique_together = ("coach", "member", "plan")

    def __str__(self) -> str:
        return f"{self.title}"
