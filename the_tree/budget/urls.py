from django.urls import path

from budget.views import (
    AccountDetailView,
    AccountListView,
    BudgetDetailView,
    BudgetListView,
    CurrencyDetailView,
    CurrencyListView,
)


urlpatterns = [
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('currencies/', CurrencyListView.as_view(), name='currency-list'),
    path('currencies/<int:pk>/', CurrencyDetailView.as_view(), name='currency-detail'),
]
