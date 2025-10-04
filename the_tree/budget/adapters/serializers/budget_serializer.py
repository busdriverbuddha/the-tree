from rest_framework import serializers
from budget.models import Budget


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Budget
