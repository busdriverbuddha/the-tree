# api/views.py

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .permissions import IsUserOrStaff
from .serializers import UserSerializer

User = get_user_model()


class UserListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsUserOrStaff]
    queryset = User.objects.all()
    serializer_class = UserSerializer
