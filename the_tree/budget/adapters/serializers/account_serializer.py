# budget/adapters/serializers/account_serializer.py

from rest_framework import serializers
from budget.models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Account
