# budget/admin.py

from django.contrib import admin

from .models import (
    Account,
    Budget,
    Category,
    Currency,
    Flow,
    Payee,
    Supercategory,
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["code", "name"]


@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    pass


@admin.register(Payee)
class PayeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Supercategory)
class SupercategoryAdmin(admin.ModelAdmin):
    pass
