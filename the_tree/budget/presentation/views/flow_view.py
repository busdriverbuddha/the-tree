# budget/presentation/views/flow_view.py

from budget.models import Flow
from budget.permissions import IsBudgetOwner
from budget.serializers import FlowSerializer

from rest_framework import generics


class FlowListView(generics.ListCreateAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer


class FlowDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsBudgetOwner]
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer
