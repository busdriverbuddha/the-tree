# budget/presentation/views/budget_view.py

from budget.models import Budget
from budget.serializers import BudgetSerializer

from rest_framework import generics


class BudgetListView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
