from rest_framework.reverse import reverse
from rest_framework import serializers
from jobs.models.job import Job


class JobSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = [
            "url",
            "id",
            "title",
            "description",
            "requirements",
            "details",
            "skills",
            "job_type",
            "salary",
            "is_available",
            "created_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
        }

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            fields["title"].required = False
        return fields

    def validate_job_type(self, value):
        if value not in ("fulltime", "parttime"):
            raise serializers.ValidationError(
                "job_type must be 'fulltime' or 'parttime'"
            )
        return value

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        return reverse(
            "api:jobs:JobRetrieveUpdateDestroy",
            kwargs={"pk": obj.id},
            request=request,
        )
