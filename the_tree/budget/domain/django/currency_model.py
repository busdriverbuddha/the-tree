# budget/domain/django/currency_model.py

from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name = "currency"
        verbose_name_plural = "currencies"

    def __repr__(self) -> str:
        return f"Currency({self.pk}: {self.code} - {self.name})"

    def __str__(self) -> str:
        return self.name
