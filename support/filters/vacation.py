import django_filters
from support.models.vacation import Vacation


class VacationFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        "coach__user__username", lookup_expr="icontains"
    )
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    start_at = django_filters.CharFilter(field_name="start_at", lookup_expr="icontains")
    end_at = django_filters.CharFilter(field_name="end_at", lookup_expr="icontains")

    class Meta:
        model = Vacation
        fields = [
            "username",
            "title",
            "status",
            "start_at",
            "end_at",
        ]
