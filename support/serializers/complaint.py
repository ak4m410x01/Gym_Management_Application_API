from rest_framework import serializers
from rest_framework.reverse import reverse
from authentication.utils.token import JWTToken
from support.models.complaint import Complaint
from accounts.models.member import Member


class ComplaintSerializer(serializers.ModelSerializer):
    member_username = serializers.CharField(
        source="member.user.username", read_only=True
    )
    member_url = serializers.SerializerMethodField()

    complaint_url = serializers.HyperlinkedIdentityField(
        view_name="api:support:ComplaintRetrieveUpdateDestroy",
        lookup_field="pk",
        read_only=True,
    )

    class Meta:
        model = Complaint
        fields = [
            "complaint_url",
            "title",
            "about",
            "description",
            "send_to",
            "status",
            "member_url",
            "member_username",
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
            for field_name in ("title", "about"):
                self.fields[field_name].required = False

    def validate_send_to(self, value):
        if value not in ["admin", "coach"]:
            raise serializers.ValidationError("send_to must be 'admin' or 'coach'.")
        return value

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

        member_username = payload.get("username")
        member = Member.objects.filter(user__username__iexact=member_username).first()
        validated_data["member"] = member

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("member", None)
        return super().update(instance, validated_data)
