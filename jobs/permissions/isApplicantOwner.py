from rest_framework.permissions import BasePermission


class IsApplicantOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        return request.user == obj.applicant
