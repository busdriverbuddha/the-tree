from rest_framework import serializers
from budget.models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Account
