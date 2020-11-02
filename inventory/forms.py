from django import forms
from .models import Product
from .models import Sales
from .models import Supllies
from .models import Expenditure
from .models import Employee


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'cetagory', 'supplier', 'unit_price', 'description')

class SuplliesForm(forms.ModelForm):

    class Meta:
        model = Supllies
        fields = ('details', 'supplier', 'quanitity', 'date', 'balance', 'checkedin')

class SalesForm(forms.ModelForm):

    class Meta:
        model = Sales
        fields = ('details', 'price', 'quantity', 'date', 'sold_at')


class ExpenditureForm(forms.ModelForm):

    class Meta:
        model = Expenditure
        fields = ('details', 'amount_requisitioned', 'date', 'requisitioned_by')

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_name', 'emp_email', 'emp_ID', 'date_of_employement', 'designation', 'salary', 'health_cert_no')