from django.utils import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse
from authentication.utils.token import JWTToken
from support.models.vacation import Vacation
from accounts.models.coach import Coach


class VacationSerializer(serializers.ModelSerializer):
    coach_username = serializers.CharField(source="coach.user.username", read_only=True)
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
            "status",
            "coach_url",
            "coach_username",
            "created_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "status": {"read_only": True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            self.fields["status"].read_only = False
            for field_name in ("title", "start_at", "end_at"):
                self.fields[field_name].required = False

    def validate_status(self, value):
        if value not in ("refused", "accepted"):
            raise serializers.ValidationError("status must be 'refused' or 'accepted'.")
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
        request = self.context.get("request")

        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        coach_username = payload.get("username")
        coach = Coach.objects.filter(user__username__iexact=coach_username).first()
        validated_data["coach"] = coach

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("coach", None)
        return super().update(instance, validated_data)
