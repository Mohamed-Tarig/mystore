from django.urls import path
from products.views import product_add, product_details, product_edit, products_list

urlpatterns = [
path('products/', products_list, name="products_list"),
path('products/add', product_add, name="product_add"),
path('products/<pk>', product_details, name="product_details"),
path('products/edit/<pk>', product_edit, name="product_edit")
]