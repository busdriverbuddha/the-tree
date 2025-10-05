# budget/adapters/serializers/payee_serializer.py

from rest_framework import serializers
from budget.models import Payee


class PayeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Payee
