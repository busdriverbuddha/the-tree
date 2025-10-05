from budget.models import Flow
from budget.serializers import FlowSerializer

from rest_framework import generics


class FlowListView(generics.ListCreateAPIView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer


class FlowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer
