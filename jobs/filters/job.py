import django_filters
from jobs.models.job import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    job_type = django_filters.CharFilter(field_name="job_type", lookup_expr="icontains")
    is_available = django_filters.CharFilter(
        field_name="is_available", lookup_expr="icontains"
    )

    class Meta:
        model = Job
        fields = [
            "title",
            "job_type",
            "is_available",
        ]
