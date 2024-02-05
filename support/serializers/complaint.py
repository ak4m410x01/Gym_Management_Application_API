from rest_framework import serializers
from rest_framework.reverse import reverse
from support.models.complaint import Complaint
from accounts.models.member import Member
from accounts.models.user import User


class ComplaintSerializer(serializers.ModelSerializer):
    member_username = serializers.CharField(source="member.user.username")
    member_first_name = serializers.CharField(
        source="member.user.first_name", read_only=True
    )
    member_last_name = serializers.CharField(
        source="member.user.last_name", read_only=True
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
            "created_at",
            "send_to",
            "status",
            "member_url",
            "member_username",
            "member_first_name",
            "member_last_name",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "status": {"read_only": True},
            "send_to": {"required": True},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = ("title", "about", "send_to", "member_username")
            for field_name in NOT_REQUIRED_FILEDS:
                self.fields[field_name].required = False

    def validate_send_to(self, value):
        if value not in ["admin", "coach"]:
            raise serializers.ValidationError("send_to must be 'admin' or 'coach'.")
        return value

    def validate_member_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if not qs.exists():
            raise serializers.ValidationError(f"{value} account does not exists.")
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
        member_data = validated_data.pop("member")
        member_username = member_data["user"]["username"]

        member = Member.objects.filter(user__username__iexact=member_username).first()
        validated_data["member"] = member

        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("member", None)
        return super().update(instance, validated_data)
