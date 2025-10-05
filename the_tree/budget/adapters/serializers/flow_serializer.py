# budget/adapters/serializers/flow_serializer.py

from rest_framework import serializers
from budget.models import Flow


class FlowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Flow
