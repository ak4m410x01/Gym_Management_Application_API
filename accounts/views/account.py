from rest_framework.generics import ListAPIView

from accounts.models.account import Account
from accounts.serializers.account import AccountSerializer


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
