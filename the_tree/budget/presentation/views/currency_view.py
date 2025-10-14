# budget/presentation/views/currency_view.py

from budget.models import Currency
from budget.permissions import CurrencyPermission
from budget.serializers import CurrencySerializer

from rest_framework import generics


class CurrencyListView(generics.ListCreateAPIView):
    permission_classes = [CurrencyPermission]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CurrencyPermission]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
