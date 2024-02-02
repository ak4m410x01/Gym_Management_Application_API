from rest_framework import serializers
from rest_framework.reverse import reverse

from accounts.models.user import User, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        ordering = (id,)
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="contact.phone")
    whatsapp = serializers.CharField(source="contact.whatsapp")
    telegram = serializers.CharField(source="contact.telegram")
    facebook = serializers.CharField(source="contact.facebook")
    instagram = serializers.CharField(source="contact.instagram")
    twitter = serializers.CharField(source="contact.twitter")

    role = serializers.SerializerMethodField()
    role_id = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "role",
            "role_id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "city",
            "address",
            "phone",
            "whatsapp",
            "telegram",
            "facebook",
            "instagram",
            "twitter",
            "is_active",
            "is_staff",
            "is_superuser",
            "is_verified",
            "last_login",
            "date_joined",
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

    def get_role_id(self, obj):
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
            kwargs={"pk": obj.pk},
            request=request,
        )
