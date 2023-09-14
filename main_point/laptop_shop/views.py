from django.shortcuts import render
from django.db.models import Count
from .models import Product, Collection


def home(request):
    products = Product.objects.all()
    collections = Collection.objects.annotate(product_count=Count('product')).filter(product_count__gt=0)
    return render(request, 'laptop_shop/home.html', {'products': products, 'collections': collections})


def index(request):
    products = Product.objects.all()
    return render(request, 'laptop_shop/index.html', {'products': products})


def show(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'laptop_shop/show.html', {'product': None})
