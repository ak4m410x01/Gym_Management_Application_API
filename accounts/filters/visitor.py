import django_filters
from accounts.models.visitor import Visitor


class VisitorFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name="account__username",
        lookup_expr="icontains",
    )

    email = django_filters.CharFilter(
        field_name="account__username",
        lookup_expr="icontains",
    )

    first_name = django_filters.CharFilter(
        field_name="account__username",
        lookup_expr="icontains",
    )

    last_name = django_filters.CharFilter(
        field_name="account__username",
        lookup_expr="icontains",
    )

    class Meta:
        model = Visitor
        fields = ["username", "email", "first_name", "last_name"]
