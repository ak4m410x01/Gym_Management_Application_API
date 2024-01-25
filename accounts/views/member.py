from rest_framework import generics
from accounts.models.member import Member
from accounts.serializers.member import MemberSerializer


class MemberList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
