# budget/views.py

from .presentation.views.account_view import AccountDetailView, AccountListView
from .presentation.views.budget_view import BudgetDetailView, BudgetListView
from .presentation.views.currency_view import CurrencyDetailView, CurrencyListView
from .presentation.views.category_view import CategoryDetailView, CategoryListView
from .presentation.views.flow_view import FlowDetailView, FlowListView
from .presentation.views.payee_view import PayeeDetailView, PayeeListView
from .presentation.views.supercategory_view import SupercategoryDetailView, SupercategoryListView

__all__ = [
    "AccountDetailView", "AccountListView",
    "BudgetDetailView", "BudgetListView",
    "CurrencyDetailView", "CurrencyListView",
    "CategoryDetailView", "CategoryListView",
    "FlowDetailView", "FlowListView",
    "PayeeDetailView", "PayeeListView",
    "SupercategoryDetailView", "SupercategoryListView",
]
