from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'laptop_shop/index.html', {'products': products})

def show(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'laptop_shop/show.html', {'product': None })
