from django.db import models

from .budget_model import Budget


class Supercategory(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="supercategories")
    name = models.CharField(max_length=64)
