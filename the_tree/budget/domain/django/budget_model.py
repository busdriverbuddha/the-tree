from django.db import models


class Budget(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=255)
