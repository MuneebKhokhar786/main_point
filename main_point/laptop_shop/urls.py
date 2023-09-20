
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<str:collection_name>', views.index, name='index'),
    path('products/<slug:product_slug>/', views.show, name='show'),
]
