import django_filters
from support.models.complaint import Complaint


class ComplaintFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        "member__user__username", lookup_expr="icontains"
    )
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    start_at = django_filters.CharFilter(field_name="start_at", lookup_expr="icontains")
    end_at = django_filters.CharFilter(field_name="end_at", lookup_expr="icontains")

    class Meta:
        model = Complaint
        fields = [
            "username",
            "title",
            "status",
            "send_to",
        ]
