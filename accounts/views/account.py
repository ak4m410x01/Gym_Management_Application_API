from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from accounts.models.account import Account
from accounts.serializers.account import AccountSerializer
from accounts.filters.account import AccountFilter


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AccountFilter
