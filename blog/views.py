from django.shortcuts import render
from .models import *

def blog_index(request):
    blog_categories = BlogCategory.objects.order_by('-created_at')
    return render(request, 'blog/blog_index.html', {
        'blog_categories': blog_categories
    })
