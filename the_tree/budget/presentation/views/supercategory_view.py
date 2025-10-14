# budget/presentation/views/supercategory_view.py

from budget.models import Supercategory
from budget.permissions import IsBudgetOwner
from budget.serializers import SupercategorySerializer

from rest_framework import generics


class SupercategoryListView(generics.ListCreateAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Supercategory.objects.all()
    serializer_class = SupercategorySerializer


class SupercategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Supercategory.objects.all()
    serializer_class = SupercategorySerializer
