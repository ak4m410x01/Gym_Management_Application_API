from rest_framework import serializers
from jobs.models.applicant import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"
