from django.utils import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse
from support.models.vacation import Vacation
from accounts.models.coach import Coach
from accounts.models.user import User


class VacationSerializer(serializers.ModelSerializer):
    coach_username = serializers.CharField(source="coach.user.username")
    coach_first_name = serializers.CharField(
        source="coach.user.first_name", read_only=True
    )
    coach_last_name = serializers.CharField(
        source="coach.user.last_name", read_only=True
    )
    coach_url = serializers.SerializerMethodField()
    vacation_url = serializers.HyperlinkedIdentityField(
        view_name="api:support:VacationRetrieveUpdateDestroy",
        lookup_field="pk",
        read_only=True,
    )

    class Meta:
        model = Vacation
        fields = [
            "vacation_url",
            "title",
            "description",
            "reason",
            "start_at",
            "end_at",
            "created_at",
            "status",
            "coach_url",
            "coach_username",
            "coach_first_name",
            "coach_last_name",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "status": {"read_only": True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = ("title", "start_at", "end_at", "coach_username")
            for field_name in NOT_REQUIRED_FILEDS:
                self.fields[field_name].required = False

    def validate_coach_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if not qs.exists():
            raise serializers.ValidationError(f"{value} account does not exists.")
        return value

    def validate_start_at(self, value):
        if not value:
            raise serializers.ValidationError("Start date must be not None.")
        if value < timezone.now().date():
            raise serializers.ValidationError("Start date must be in the future.")
        return value

    def validate_end_at(self, value):
        if not value:
            raise serializers.ValidationError("End date must be not None.")
        if str(value) <= self.initial_data.get("start_at"):
            raise serializers.ValidationError("End date must be in the future.")

        return value

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
        coach_data = validated_data.pop("coach")
        coach_username = coach_data["user"]["username"]

        coach = Coach.objects.filter(user__username__iexact=coach_username).first()
        validated_data["coach"] = coach

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("coach", None)
        return super().update(instance, validated_data)
