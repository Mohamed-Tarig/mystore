from django.urls import path
from products.views import product_details, products_list

urlpatterns = [
path('products/', products_list, name="products_list"),
path('products/<pk>', product_details, name="product_details")
]