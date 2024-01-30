import django_filters
from accounts.models.account import Account


class AccountFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(method="filter_by_role")

    class Meta:
        model = Account
        fields = ["role"]

    def filter_by_role(self, queryset, name, value):
        if value == "admin":
            queryset = queryset.filter(admin__isnull=False)
        elif value == "coach":
            queryset = queryset.filter(coach__isnull=False)
        elif value == "member":
            queryset = queryset.filter(member__isnull=False)
        elif value == "visitor":
            queryset = queryset.filter(visitor__isnull=False)
        else:
            queryset = queryset.none()
        return queryset
