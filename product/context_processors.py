
from .models import *

def product_categories_context(request):
    return {
        'product_categories': ProductCategory.objects.all()
    }