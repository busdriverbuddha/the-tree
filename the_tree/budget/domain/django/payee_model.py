# budget/domain/django/payee_model.py

from django.db import models

from .category_model import Category


class Payee(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def owner(self):
        return self.category.supercategory.budget.owner
