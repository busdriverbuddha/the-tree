from rest_framework import serializers
from budget.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Category
