from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm


def list_products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})

def create_products(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})


def update_product(request,id):
    products = Products.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=products)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': products})


def delete_product(request, id):
    products = Products.objects.get(id=id)

    if request.method == 'POST':
        products.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'products': products})