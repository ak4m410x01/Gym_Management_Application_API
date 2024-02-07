from rest_framework import serializers
from rest_framework.reverse import reverse
from accounts.models.salary import CoachSalary
from accounts.models.coach import Coach
from accounts.models.user import User


class CoachSalarySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    coach_url = serializers.SerializerMethodField(read_only=True)
    coach_username = serializers.CharField(source="coach.user.username")

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

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            fields["salary"].required = False
            fields["coach_username"].read_only = True
        return fields

    def validate_coach_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if not qs.exists():
            raise serializers.ValidationError("coach account does not exists")

        qs = CoachSalary.objects.filter(coach__user__username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("coach already have salary.")

        return value

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:accounts:CoachSalaryRetrieveUpdateDestroy",
            kwargs={"pk": obj.id},
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
        coach = validated_data.pop("coach", {})
        coach = Coach.objects.filter(
            user__username__iexact=coach["user"]["username"]
        ).first()
        return CoachSalary.objects.create(coach=coach, **validated_data)
