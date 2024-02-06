from rest_framework import serializers
from rest_framework.reverse import reverse
from accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "role",
            "username",
            "first_name",
            "last_name",
        ]

    def get_role(self, obj):
        if hasattr(obj, "admin"):
            return "admin"
        elif hasattr(obj, "coach"):
            return "coach"
        elif hasattr(obj, "member"):
            return "member"
        elif hasattr(obj, "visitor"):
            return "visitor"
        else:
            return None

    def get_user_id(self, obj):
        if hasattr(obj, "admin"):
            return obj.admin.id
        elif hasattr(obj, "coach"):
            return obj.coach.id
        elif hasattr(obj, "member"):
            return obj.member.id
        elif hasattr(obj, "visitor"):
            return obj.visitor.id
        else:
            return None

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        role = self.get_role(obj)
        user_id = self.get_user_id(obj)
        view_name = ""
        if role == "admin":
            view_name = "api:accounts:AdminRetrieveUpdateDestroy"
        elif role == "coach":
            view_name = "api:accounts:CoachRetrieveUpdateDestroy"
        elif role == "member":
            view_name = "api:accounts:MemberRetrieveUpdateDestroy"
        elif role == "visitor":
            view_name = "api:accounts:VisitorRetrieveUpdateDestroy"
        else:
            return None

        return reverse(
            view_name,
            kwargs={"pk": user_id},
            request=request,
        )
