# budget/presentation/views/account_view.py

from budget.models import Account
from budget.permissions import IsBudgetOwner
from budget.serializers import AccountSerializer

from rest_framework import generics


class AccountListView(generics.ListCreateAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
