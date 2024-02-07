import django_filters
from jobs.models.applicant import Applicant


class ApplicantFilter(django_filters.FilterSet):
    applicant_username = django_filters.CharFilter(
        "applicant__username", lookup_expr="icontains"
    )
    status = django_filters.CharFilter(field_name="status", lookup_expr="icontains")
    job_id = django_filters.CharFilter(field_name="job.id", lookup_expr="icontains")

    class Meta:
        model = Applicant
        fields = [
            "applicant_username",
            "status",
            "job_id",
        ]
