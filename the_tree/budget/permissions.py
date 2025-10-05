# budget/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CurrencyPermission(BasePermission):
    """
    Anyone can read; only staff can write.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        # Same logic at object level
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsBudgetOwner(BasePermission):
    """
    Only the owner of the related Budget can access.
    Applies to Budget, Account, Flow, Category, Payee, Supercategory.
    """
    def has_object_permission(self, request, view, obj):
        budget = resolve_budget_from_instance(obj)
        return bool(budget and budget.owner_id == getattr(request.user, "id", None))
