# budget/domain/django/supercategory_model.py

from django.db import models

from .budget_model import Budget


class Supercategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="supercategories")
    name = models.CharField(max_length=64)

    @property
    def owner(self):
        return self.budget.owner

    class Meta:
        verbose_name = "supercategory"
        verbose_name_plural = "supercategories"
