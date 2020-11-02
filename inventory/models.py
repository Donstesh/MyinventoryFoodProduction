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

class Supllies(models.Model):
    details = models.CharField(max_length=200, blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)
    quanitity = models.IntegerField()
    date = models.DateField()
    balance = models.DecimalField(max_digits=20, decimal_places=4, default=Decimal('0.0000'))
    checkedin = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Sales(models.Model):
    details = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    sold_at = models.DecimalField(max_digits=20, decimal_places=4, default=Decimal('0.0000'))

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_name = models.CharField(max_length=200, blank=True, null=True)
    emp_email = models.CharField(max_length=200, blank=True, null=True)
    emp_ID = models.IntegerField()
    date_of_employement = models.DateField()
    designation = models.DecimalField(max_digits=20, decimal_places=4, default=Decimal('0.0000'))
    salary = models.IntegerField()
    health_cert_no = models.IntegerField()

    def __str__(self):
        return self.name


class Expenditure(models.Model):
    details = models.CharField(max_length=200, blank=True, null=True)
    amount_requisitioned = models.CharField(max_length=200, blank=True, null=True)   
    date = models.DateField() 
    requisitioned_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name