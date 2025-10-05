# budget/domain/django/account_model.py

from django.db import models
from django.utils.translation import gettext_lazy as _

from .budget_model import Budget
from .currency_model import Currency


class Account(models.Model):

    class AccountType(models.TextChoices):
        CHECKING = "checking", _("Checking")
        CREDIT_CARD = "credit_card", _("Credit card")
        SAVINGS = "savings", _("Savings")
        CASH = "cash", _("Cash")
        # etc

    account_type = models.CharField(max_length=32, choices=AccountType.choices, editable=False)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="accounts", editable=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name="accounts", editable=False)
    name = models.CharField(max_length=128)
