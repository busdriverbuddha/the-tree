# budget/presentation/views/payee_view.py

from budget.models import Payee
from budget.permissions import IsBudgetOwner
from budget.serializers import PayeeSerializer

from rest_framework import generics


class PayeeListView(generics.ListCreateAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer


class PayeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer
