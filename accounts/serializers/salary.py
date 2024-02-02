from rest_framework import serializers

from accounts.models.coach import Coach
from accounts.models.salary import CoachSalary


class CoachSalarySerializer(serializers.ModelSerializer):
    salary_url = serializers.HyperlinkedIdentityField(
        view_name="api:accounts:CoachSalaryRetrieveUpdateDestroy",
        lookup_field="pk",
        read_only=True,
    )

    coach_id = serializers.IntegerField(source="coach.id")
    coach_username = serializers.CharField(
        source="coach.user.username", read_only=True, required=False
    )
    coach_first_name = serializers.CharField(
        source="coach.user.first_name", read_only=True
    )
    coach_last_name = serializers.CharField(
        source="coach.user.last_name", read_only=True
    )
    coach_url = serializers.HyperlinkedIdentityField(
        view_name="api:accounts:CoachRetrieveUpdateDestroy",
        lookup_field="pk",
        read_only=True,
    )

    class Meta:
        model = CoachSalary
        fields = [
            "coach_url",
            "coach_id",
            "coach_username",
            "coach_first_name",
            "coach_last_name",
            "salary_url",
            "id",
            "salary",
        ]
        extra_kwargs = {
            "salary": {"required": True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get("request") and self.context["request"].method == "PUT":
            self.fields["coach_id"].required = False
            self.fields["coach_id"].read_only = True

    def validate_coach_id(self, coach_id: int) -> str:
        if not Coach.objects.filter(id=coach_id).exists():
            raise serializers.ValidationError(f"coach account does not exists.")
        if CoachSalary.objects.filter(coach=coach_id).exists():
            raise serializers.ValidationError(f"coach salary already exists.")
        return coach_id

    def create(self, validated_data):
        coach_data = validated_data.pop("coach")
        coach = Coach.objects.filter(id=coach_data.get("id")).first()
        coach_salary = CoachSalary.objects.create(coach=coach, **validated_data)
        return coach_salary
