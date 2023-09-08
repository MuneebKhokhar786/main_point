from django.shortcuts import render
from .models import Product, Collection

def index(request):
    products = Product.objects.all()
    collections = Collection.objects.all()
    return render(request, 'laptop_shop/index.html', {'products': products, 'collections': collections})


def show(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'laptop_shop/show.html', {'product': None })
