import django_filters

from accounts.models.user import User


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(method="filter_by_role")
    username = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["role", "username", "email", "first_name", "last_name"]

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
