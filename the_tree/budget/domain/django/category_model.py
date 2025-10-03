from django.db import models

from .budget_model import Budget
from .supercategory_model import Supercategory

class Category(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="categories")
    supercategory = models.ForeignKey(Supercategory, on_delete=models.CASCADE, related_name="categories")
