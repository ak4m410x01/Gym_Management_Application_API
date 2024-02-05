from django.db import models


class Job(models.Model):
    CATEGORY = (
        ("fulltime", "fulltime"),
        ("parttime", "parttime"),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10_000, blank=True, null=True)
    requirements = models.CharField(max_length=10_000, blank=True, null=True)
    details = models.CharField(max_length=10_000, blank=True, null=True)
    skills = models.CharField(max_length=10_000, blank=True, null=True)
    job_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    salary = models.IntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"
