# budget/domain/django/budget_model.py
from django.contrib.auth import get_user_model
from django.db import models


class Budget(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="budgets",
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=255)
