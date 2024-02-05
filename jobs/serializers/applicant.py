from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.reverse import reverse
from jobs.models.applicant import Applicant
from accounts.models.user import User


class ApplicantSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    job_url = serializers.SerializerMethodField(read_only=True)
    job_title = serializers.CharField(source="job.title", read_only=True)

    applicant_url = serializers.SerializerMethodField(read_only=True)
    applicant_role = serializers.SerializerMethodField(read_only=True)
    applicant_username = serializers.CharField(source="applicant.username")

    class Meta:
        model = Applicant
        fields = [
            "url",
            "status",
            "job_url",
            "job_title",
            "applicant_url",
            "applicant_role",
            "applicant_username",
            "applied_at",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            self.fields["applicant_username"].required = False
            self.fields["applicant_username"].read_only = True

    def validate_status(self, value):
        if value not in ("refused", "accepted"):
            raise serializers.ValidationError("Enter 'refused' or 'accepted'.")
        return value

    def validate_applicant_username(self, value):
        user = User.objects.filter(username__iexact=value)
        if not user.exists():
            raise serializers.ValidationError(f"{value} account does not exists.")

        job_id = self.context["view"].kwargs["pk"]

        applicant = Applicant.objects.filter(
            applicant__username__iexact=value, job=job_id
        )
        if applicant.exists():
            raise serializers.ValidationError(f"{value} already applied.")

        return value

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None
        return reverse(
            "api:jobs:ApplicantRetrieveUpdateDestroy",
            kwargs={"job_id": obj.job.id, "applicant_id": obj.id},
            request=request,
        )

    def get_job_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None
        return reverse(
            "api:jobs:JobRetrieveUpdateDestroy",
            kwargs={"pk": obj.job.id},
            request=request,
        )

    def get_applicant_role(self, obj):
        applicant = obj.applicant
        if hasattr(applicant, "admin"):
            return "admin"
        elif hasattr(applicant, "coach"):
            return "coach"
        elif hasattr(applicant, "member"):
            return "member"
        elif hasattr(applicant, "visitor"):
            return "visitor"
        else:
            return None

    def get_applicant_id(self, obj):
        applicant = obj.applicant
        if hasattr(applicant, "admin"):
            return applicant.admin.id
        elif hasattr(applicant, "coach"):
            return applicant.coach.id
        elif hasattr(applicant, "member"):
            return applicant.member.id
        elif hasattr(applicant, "visitor"):
            return applicant.visitor.id
        else:
            return None

    def get_applicant_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        applicant_role = self.get_applicant_role(obj)
        applicant_id = self.get_applicant_id(obj)

        view_name = ""
        if applicant_role == "admin":
            view_name = "api:accounts:AdminRetrieveUpdateDestroy"
        elif applicant_role == "coach":
            view_name = "api:accounts:CoachRetrieveUpdateDestroy"
        elif applicant_role == "member":
            view_name = "api:accounts:MemberRetrieveUpdateDestroy"
        elif applicant_role == "visitor":
            view_name = "api:accounts:VisitorRetrieveUpdateDestroy"
        else:
            return None

        return reverse(view_name, kwargs={"pk": applicant_id}, request=request)

    def create(self, validated_data):
        username = validated_data["applicant"]["username"]
        user = User.objects.filter(username__iexact=username).first()

        job_id = self.context["view"].kwargs["pk"]
        return Applicant.objects.create(applicant=user, job_id=job_id)
