# budget/domain/django/category_model.py

from django.db import models

from .supercategory_model import Supercategory


class Category(models.Model):
    supercategory = models.ForeignKey(Supercategory, on_delete=models.CASCADE, related_name="categories")

    @property
    def owner(self):
        return self.supercategory.owner

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
