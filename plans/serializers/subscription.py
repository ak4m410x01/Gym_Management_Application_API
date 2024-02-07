from rest_framework import serializers
from rest_framework.reverse import reverse
from plans.models.subscription import Subscription
from authentication.utils.token import JWTToken
from accounts.models.visitor import Visitor
from accounts.models.member import Member


class SubscriptionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:plans:SubscriptionRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    plan_url = serializers.SerializerMethodField(read_only=True)
    plan_title = serializers.CharField(source="plan.title", read_only=True)

    coach_url = serializers.SerializerMethodField(read_only=True)
    coach_username = serializers.CharField(source="coach.user.username", read_only=True)

    member_url = serializers.SerializerMethodField(read_only=True)
    member_username = serializers.CharField(
        source="member.user.username", read_only=True
    )

    class Meta:
        model = Subscription
        fields = [
            "url",
            "is_finished",
            "subscribed_at",
            "plan_url",
            "plan",
            "plan_title",
            "coach_url",
            "coach",
            "coach_username",
            "member_url",
            "member",
            "member_username",
        ]
        extra_kwargs = {
            "is_finished": {"read_only": True},
            "member": {"read_only": True},
        }

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            fields["is_finished"].read_only = False
            for field_name in ("plan", "coach"):
                fields[field_name].required = False
        return fields

    def get_plan_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:plans:PlanRetrieveUpdateDestroy",
            kwargs={"pk": obj.plan.id},
            request=request,
        )

    def get_coach_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:accounts:CoachRetrieveUpdateDestroy",
            kwargs={"pk": obj.member.id},
            request=request,
        )

    def get_member_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:accounts:MemberRetrieveUpdateDestroy",
            kwargs={"pk": obj.member.id},
            request=request,
        )

    def create(self, validated_data):
        request = self.context.get("request")
        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)

        if payload["user_role"] == "member":
            member = Member.objects.filter(user__username=payload["username"]).first()
            print(member)

        elif payload["user_role"] == "visitor":
            visitor = Visitor.objects.filter(id=payload["user_id"]).first()
            if not visitor:
                raise serializers.ValidationError({"user": "Not found."})

            member = Member.objects.create(user=visitor.user)
            visitor.delete()

        validated_data["member"] = member
        return super().create(validated_data)
