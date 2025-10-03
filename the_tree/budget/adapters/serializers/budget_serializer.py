from rest_framework import serializers
from budget.models import Budget


class BudgetSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Budget
