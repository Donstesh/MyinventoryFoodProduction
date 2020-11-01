from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'inventory/index.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/detail.html', {'product': product})


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


#
