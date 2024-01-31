from rest_framework import serializers
from accounts.models.account import Account


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = Account
        fields = ["token"]
