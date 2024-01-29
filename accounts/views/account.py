from rest_framework.generics import ListAPIView

from ..models.account import Account
from ..serializers.account import AccountSerializer


class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
