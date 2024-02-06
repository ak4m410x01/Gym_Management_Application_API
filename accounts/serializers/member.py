from re import match
from datetime import datetime, date
from rest_framework import serializers
from accounts.models.member import Member
from accounts.models.user import User, Contact


class BaseMemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")
    password = serializers.CharField(source="user.password", write_only=True)

    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    gender = serializers.CharField(source="user.gender")
    date_of_birth = serializers.DateField(source="user.date_of_birth")

    city = serializers.CharField(source="user.city", required=False)
    address = serializers.CharField(source="user.address", required=False)

    phone = serializers.CharField(source="user.contact.phone", required=False)
    whatsapp = serializers.CharField(source="user.contact.whatsapp", required=False)
    telegram = serializers.CharField(source="user.contact.telegram", required=False)
    facebook = serializers.CharField(source="user.contact.facebook", required=False)
    instagram = serializers.CharField(source="user.contact.instagram", required=False)
    twitter = serializers.CharField(source="user.contact.twitter", required=False)

    last_login = serializers.DateTimeField(
        source="user.last_login",
        required=False,
        read_only=True,
    )

    date_joined = serializers.DateTimeField(
        source="user.date_joined",
        required=False,
        read_only=True,
    )

    url = serializers.HyperlinkedIdentityField(
        view_name="api:accounts:MemberRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    class Meta:
        model = Member
        ordering = (id,)
        fields = [
            "url",
            "username",
            "email",
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
            "last_login",
            "date_joined",
        ]

    def validate_username(self, value: str) -> str:
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already used. try another one!")

        regex = r"^[a-zA-Z_][A-Za-z0-9_\.]+$"
        if not match(regex, value):
            raise serializers.ValidationError("Invalid username :(")

        return value

    def validate_email(self, value: str) -> str:
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already used. try another one!")
        return value

    def validate_gender(self, value: str) -> str:
        regex = r"^[mf]$"
        if not match(regex, value):
            raise serializers.ValidationError(f"gender must be 'm' or 'f'.")
        return value

    def validate_date_of_birth(self, value: str) -> str:
        if isinstance(value, date):
            value = value.strftime("%Y-%m-%d")

        try:
            dob = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise serializers.ValidationError(
                "Date of birth must be in the format YYYY-MM-DD."
            )

        if dob.date() > datetime.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future.")

        return value

    def validate_phone(self, value: str) -> str:
        regex = r"^\+201[0125]\d{8}$"
        if not match(regex, value):
            raise serializers.ValidationError(
                "Egyptian phone number must be like: '+201234567890'"
            )

        return value

    def validate_whatsapp(self, value: str) -> str:
        regex = r"^https://wa\.me/201[0125]\d{8}$"
        if not match(regex, value):
            raise serializers.ValidationError(
                "Egyptian whatsapp link must be like: 'https://wa.me/201234567890'"
            )
        return value

    def validate_telegram(self, value: str) -> str:
        regex = r"^https://t\.me/[A-Za-z0-9_]{1,}$"
        if not match(regex, value):
            raise serializers.ValidationError("Invalid Telegram Link :(")
        return value

    def validate_facebook(self, value: str) -> str:
        regex = r"^https://www\.facebook\.com/[A-Za-z0-9.]+$"
        if not match(regex, value):
            raise serializers.ValidationError("Invalid Facebook Link :(")
        return value

    def validate_instagram(self, value: str) -> str:
        regex = r"^https://www\.instagram\.com/[A-Za-z0-9_\.]+$"
        if not match(regex, value):
            raise serializers.ValidationError("Invalid Instagram Link :(")
        return value

    def validate_twitter(self, value: str) -> str:
        regex = r"^https://(?:twitter|x)\.com/[A-Za-z0-9_]{1,15}$"
        if not match(regex, value):
            raise serializers.ValidationError("Invalid Twitter Link :(")
        return value


class MemberSerializer(BaseMemberSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "email",
                "username",
                "password",
                "first_name",
                "last_name",
                "gender",
                "date_of_birth",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                self.fields[field_name].required = False

    def create(self, validated_data):
        user_data = validated_data.pop("user", {})
        contact_data = user_data.pop("contact", {})

        contact = Contact.objects.create(**contact_data)
        user = User.objects.create(contact=contact, **user_data)
        member = Member.objects.create(user=user, **validated_data)

        return member

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        contact_data = user_data.pop("contact", {})

        # Contact Model
        for key, value in contact_data.items():
            setattr(instance.user.contact, key, value)
        instance.user.contact.save()

        # User Model
        for key, value in user_data.items():
            setattr(instance.user, key, value)
        instance.user.save()

        # Admin Model
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
