from django.db import models
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    cetagory = models.CharField(max_length=200, blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=4, default=Decimal('0.0000'))
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Id:{0} Name:{1}'.format(self.id, self.name)
