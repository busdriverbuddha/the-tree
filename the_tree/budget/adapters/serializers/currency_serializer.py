from rest_framework import serializers
from budget.models import Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Currency
