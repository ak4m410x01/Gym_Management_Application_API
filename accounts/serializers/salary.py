from rest_framework import serializers
from rest_framework.reverse import reverse
from accounts.models.coach import Coach
from accounts.models.salary import CoachSalary


class CoachSalarySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    coach_url = serializers.SerializerMethodField(read_only=True)
    coach_username = serializers.CharField(source="coach.user.username", read_only=True)

    class Meta:
        model = CoachSalary
        fields = [
            "url",
            "salary",
            "coach_url",
            "coach_username",
        ]
        extra_kwargs = {
            "salary": {"required": True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            self.fields["salary"].required = False

    def validate_salary(self, value):
        request = self.context.get("request")
        if request and request.method == "PUT":
            return value

        coach_id = self.context["view"].kwargs["coach_id"]
        qs = CoachSalary.objects.filter(coach=coach_id)
        if qs.exists():
            raise serializers.ValidationError("coach already have salary.")

        qs = Coach.objects.filter(id=coach_id)
        if not qs.exists():
            raise serializers.ValidationError("coach account does not exists")
        return value

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:accounts:CoachSalaryRetrieveUpdateDestroy",
            kwargs={"coach_id": obj.coach.id, "salary_id": obj.id},
            request=request,
        )

    def get_coach_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:accounts:CoachRetrieveUpdateDestroy",
            kwargs={"pk": obj.coach.id},
            request=request,
        )

    def create(self, validated_data):
        coach_id = self.context["view"].kwargs["coach_id"]
        coach = Coach.objects.filter(id=coach_id).first()

        salary_id = validated_data["salary"]
        return CoachSalary.objects.create(coach=coach, salary=salary_id)
