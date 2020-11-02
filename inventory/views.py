from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm
from .models import Supllies
from .forms import SuplliesForm
from .models import Sales
from .forms import SalesForm
from .models import Expenditure
from .forms import ExpenditureForm
from .models import Employee
from .forms import EmployeeForm



"""
DISPLAY FUNCTIONS
"""

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/index.html', context)

def supllies(request):
    supllies = Supllies.objects.all()
    context = {'supllies': supllies}
    return render(request, 'inventory/suplies/index.html', context)

def sales(request):
    sales = Sales.objects.all()
    context = {'sales': sales}
    return render(request, 'inventory/sales/index.html', context)

def expenditures(request):
    expenditures = Expenditure.objects.all()
    context = {'expenditures': expenditures}
    return render(request, 'inventory/expenditures/index.html', context)

def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'inventory/employees/index.html', context)

"""
DETAILS FUNCTIONS
"""
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/detail.html', {'product': product})

"""
ADD FUNCTIONS
"""

def addnew(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'inventory/new.html', {'form': form})

def addsupllier(request):
    if request.method == 'POST':
        form = SuplliesForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
        return redirect('supplies')

    else:
        form = SuplliesForm()
    return render(request, 'inventory/suplies/new.html', {'form': form})


def addsale(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
        return render(request, 'inventory/sales/index.html')

    else:
        form = SuplliesForm()
    return render(request, 'inventory/sales/new.html', {'form': form})


def addexp(request):
    if request.method == 'POST':
        form = ExpenditureForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
        return render(request, 'inventory/expenditures/index.html')

    else:
        form = SuplliesForm()
    return render(request, 'inventory/expenditures/new.html', {'form': form})

def addemployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(dir(form))
        if form.is_valid():
            form.save()
        return render(request, 'inventory/employees/index.html')

    else:
        form = EmployeeForm()
    return render(request, 'inventory/employees/new.html', {'form': form})



"""
EDIT FUNCTIONS
"""

def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit.html', {'form': form})

def editsuply(request, pk):
    supllies = get_object_or_404(Supllies, pk=pk)
    if request.method == "POST":
        form = SuplliesForm(request.POST, instance=supllies)
        if form.is_valid():
            form.save()
            return redirect('suplies/index')
    else:
        form = SuplliesForm(instance=supllies)
    return render(request, 'inventory/suplies/edit.html', {'form': form})

def editsale(request, pk):
    sales = get_object_or_404(Sales, pk=pk)
    if request.method == "POST":
        form = SalesForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()
            return redirect('sales/index')
    else:
        form = SalesForm(instance=sales)
    return render(request, 'inventory/sales/edit.html', {'form': form})

def editexp(request, pk):
    expenditures = get_object_or_404(Expenditure, pk=pk)
    if request.method == "POST":
        form = ExpenditureForm(request.POST, instance=expenditures)
        if form.is_valid():
            form.save()
            return redirect('expenditures/index')
    else:
        form = ExpenditureForm(instance=Expenditure)
    return render(request, 'inventory/expenditures/edit.html', {'form': form})

def editemp(request, pk):
    employees = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect('employees/index')
    else:
        form = EmployeeForm(instance=employees)
    return render(request, 'inventory/employees/edit.html', {'form': form})

