import django_filters

from accounts.models.salary import CoachSalary


class SalaryFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name="coach__user__username", lookup_expr="icontains"
    )
    class Meta:
        model = CoachSalary
        fields = ["username"]
