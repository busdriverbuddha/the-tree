# budget/permissions.py

from rest_framework.permissions import BasePermission


class IsUserOrStaff(BasePermission):
    """
    Only the owner of the related Budget can access.
    Applies to Budget, Account, Flow, Category, Payee, Supercategory.
    """
    def has_object_permission(self, request, view, obj):  # type: ignore
        if not request.user.is_authenticated:
            return False
        return request.user.is_staff or obj == request.user
