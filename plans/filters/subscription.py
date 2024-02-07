import django_filters
from plans.models.subscription import Subscription


class SubscriptionFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(field_name="price", lookup_expr="icontains")
    is_finished = django_filters.CharFilter(
        field_name="is_finished", lookup_expr="icontains"
    )
    plan = django_filters.CharFilter(field_name="plan", lookup_expr="icontains")
    coach = django_filters.CharFilter(field_name="coach", lookup_expr="icontains")
    member_username = django_filters.CharFilter(
        field_name="member_username", lookup_expr="icontains"
    )

    class Meta:
        model = Subscription
        fields = [
            "price",
            "is_finished",
            "plan",
            "coach",
            "member_username",
        ]
