from rest_framework import serializers
from budget.models import Payee


class PayeeSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Payee
