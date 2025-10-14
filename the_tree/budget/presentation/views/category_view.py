# budget/presentation/views/category_view.py

from budget.models import Category
from budget.permissions import IsBudgetOwner
from budget.serializers import CategorySerializer

from rest_framework import generics


class CategoryListView(generics.ListCreateAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
