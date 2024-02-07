from accounts.serializers.visitor import BaseVisitorSerializer
from accounts.models.user import User, Contact
from accounts.models.visitor import Visitor


class SignUpSerializer(BaseVisitorSerializer):
    def create(self, validated_data):
        user_data = validated_data.pop("user", {})
        contact_data = user_data.pop("contact", {})

        contact = Contact.objects.create(**contact_data)
        user = User.objects.create(contact=contact, **user_data)
        return Visitor.objects.create(user=user, **validated_data)
