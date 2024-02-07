from rest_framework import serializers
from plans.models.plan import Plan


class PlanSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        "api:plans:PlanRetrieveUpdateDestroy", lookup_field="pk"
    )

    class Meta:
        model = Plan
        fields = [
            "url",
            "id",
            "title",
            "description",
            "price",
            "classes",
            "max_days",
            "created_at",
            "updated_at",
        ]
