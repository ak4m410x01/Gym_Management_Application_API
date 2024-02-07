import django_filters
from plans.models.plan import Plan


class PlanFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    price = django_filters.CharFilter(field_name="price", lookup_expr="icontains")
    classes = django_filters.CharFilter(field_name="classes", lookup_expr="icontains")
    max_days = django_filters.CharFilter(field_name="max_days", lookup_expr="icontains")

    class Meta:
        model = Plan
        fields = [
            "title",
            "price",
            "classes",
            "max_days",
        ]
