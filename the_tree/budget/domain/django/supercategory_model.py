from django.db import models


class Supercategory(models.Model):
    name = models.CharField(max_length=64)
