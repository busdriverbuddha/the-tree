# budget/presentation/views/supercategory_view.py

from budget.models import Supercategory
from budget.serializers import SupercategorySerializer

from rest_framework import generics


class SupercategoryListView(generics.ListCreateAPIView):
    queryset = Supercategory.objects.all()
    serializer_class = SupercategorySerializer


class SupercategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supercategory.objects.all()
    serializer_class = SupercategorySerializer
