# budget/presentation/views/budget_view.py

from budget.models import Budget
from budget.permissions import IsBudgetOwner
from budget.serializers import BudgetSerializer

from rest_framework import generics


class BudgetListView(generics.ListCreateAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def perform_create(self, serializer):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        serializer.save(owner=user)


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
