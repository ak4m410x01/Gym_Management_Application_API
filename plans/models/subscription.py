from django.db import models
from django.utils import timezone
from accounts.models.coach import Coach
from accounts.models.member import Member
from plans.models.plan import Plan


class Subscription(models.Model):
    subscribed_at = models.DateTimeField(auto_now_add=True)

    plan = models.ForeignKey(Plan, models.CASCADE)
    coach = models.ForeignKey(Coach, models.CASCADE)
    member = models.ForeignKey(Member, models.CASCADE)

    @property
    def is_finished(self) -> bool:
        end_date = self.subscribed_at + timezone.timedelta(days=self.plan.max_days)
        return end_date.date() <= timezone.now().date()

    def __str__(self) -> str:
        return f"{self.member.user.username}"
