from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..models.member import Member
from ..serializers.member import MemberSerializer


class MemberListCreate(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
