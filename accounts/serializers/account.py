from rest_framework import serializers
from accounts.models.account import Account, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        ordering = (id,)
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="contact.phone")
    whatsapp = serializers.CharField(source="contact.whatsapp")
    telegram = serializers.CharField(source="contact.telegram")
    facebook = serializers.CharField(source="contact.facebook")
    instagram = serializers.CharField(source="contact.instagram")
    twitter = serializers.CharField(source="contact.twitter")

    role = serializers.SerializerMethodField()
    role_id = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
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
            "first_login",
            "last_login",
            "joined_at",
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
