from django.db import models

from .supercategory_model import Supercategory


class Category(models.Model):
    supercategory = models.ForeignKey(Supercategory, on_delete=models.CASCADE, related_name="categories")
