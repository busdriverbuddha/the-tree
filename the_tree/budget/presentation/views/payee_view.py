from budget.models import Payee
from budget.serializers import PayeeSerializer

from rest_framework import generics


class PayeeListView(generics.ListCreateAPIView):
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer


class PayeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer
