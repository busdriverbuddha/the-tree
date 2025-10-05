from rest_framework import serializers
from budget.models import Supercategory


class SupercategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = Supercategory
