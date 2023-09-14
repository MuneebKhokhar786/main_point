
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.index, name='index'),
    path('<int:product_id>/', views.show, name='show'),
]
