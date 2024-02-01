from rest_framework import serializers
from accounts.models.user import User


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ["token"]
