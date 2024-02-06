import django_filters

from accounts.models.visitor import Visitor


class VisitorFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(
        field_name="user__username", lookup_expr="icontains"
    )
    email = django_filters.CharFilter(field_name="user__email", lookup_expr="icontains")
    first_name = django_filters.CharFilter(
        field_name="user__first_name", lookup_expr="icontains"
    )
    last_name = django_filters.CharFilter(
        field_name="user__last_name", lookup_expr="icontains"
    )
    gender = django_filters.CharFilter(
        field_name="user__gender", lookup_expr="icontains"
    )

    class Meta:
        model = Visitor
        fields = ["username", "email", "first_name", "last_name", "gender"]
