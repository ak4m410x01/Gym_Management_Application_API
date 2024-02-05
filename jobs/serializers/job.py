from rest_framework import serializers
from rest_framework.fields import empty
from jobs.models.job import Job


class JobSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:jobs:JobRetrieveUpdateDestroy", lookup_field="pk", read_only=True
    )

    class Meta:
        model = Job
        fields = [
            "url",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.method == "PUT":
            self.fields["title"].required = False

    def validate_job_type(self, value):
        if value not in ("fulltime", "parttime"):
            raise serializers.ValidationError(
                "job_type must be 'fulltime' or 'parttime'"
            )
        return value
