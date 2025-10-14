# budget/domain/django/flow_model.py

from django.db import models
from django.utils.translation import gettext_lazy as _

from .currency_model import Currency
from .account_model import Account
from .payee_model import Payee


class Flow(models.Model):

    class FlowType(models.TextChoices):
        INFLOW = "inflow", _("Inflow")
        OUTFLOW = "outflow", _("Outflow")

    created_at = models.DateTimeField(auto_now_add=True)
    bank_date = models.DateField(help_text="The actual date registered at the payment provider.")

    flow_type = models.CharField(max_length=16, choices=FlowType.choices)

    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    amount_cents = models.PositiveIntegerField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE, blank=True, null=True)
    transfer = models.ForeignKey("Flow", on_delete=models.CASCADE, blank=True, null=True)

    comments = models.TextField(blank=True, null=True)

    def owner(self):
        return self.account.budget.owner
