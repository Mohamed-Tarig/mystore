from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products-list.html', {'products': products})

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product-details.html', {'product': product})
