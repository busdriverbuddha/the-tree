from django.urls import path

from budget.views import (
    AccountDetailView, AccountListView,
    BudgetDetailView, BudgetListView,
    CurrencyDetailView, CurrencyListView,
    CategoryDetailView, CategoryListView,
    FlowDetailView, FlowListView,
    PayeeDetailView, PayeeListView,
    SupercategoryDetailView, SupercategoryListView,
)

urlpatterns = [
    path('accounts/', AccountListView.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),

    path('budgets/', BudgetListView.as_view(), name='budget-list'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),

    path('currencies/', CurrencyListView.as_view(), name='currency-list'),
    path('currencies/<int:pk>/', CurrencyDetailView.as_view(), name='currency-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('flows/', FlowListView.as_view(), name='flow-list'),
    path('flows/<int:pk>/', FlowDetailView.as_view(), name='flow-detail'),

    path('payees/', PayeeListView.as_view(), name='payee-list'),
    path('payees/<int:pk>/', PayeeDetailView.as_view(), name='payee-detail'),

    path('supercategories/', SupercategoryListView.as_view(), name='supercategory-list'),
    path('supercategories/<int:pk>/', SupercategoryDetailView.as_view(), name='supercategory-detail'),
]
