from rest_framework import serializers



from accounts.models.account import Account


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username:
            raise serializers.ValidationError("Username is required.")
        if not password:
            raise serializers.ValidationError("Password is required.")
        
        return data
