from django.shortcuts import render

# Create your views here.
def product_index(request):
    return render(request, 'product/product_index.html')

def product_detail(request, product_slug=None):
    return render(request, 'product/product_detail.html')