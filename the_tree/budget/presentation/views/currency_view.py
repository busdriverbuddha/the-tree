# budget/presentation/views/currency_view.py

from budget.models import Currency
from budget.serializers import CurrencySerializer

from rest_framework import generics


class CurrencyListView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
