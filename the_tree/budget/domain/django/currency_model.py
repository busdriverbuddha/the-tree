from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=3, unique=True)
