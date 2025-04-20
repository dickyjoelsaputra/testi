from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

def blog_index(request, category_slug=None):
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
    
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        blogs = blogs.filter(categories=category)
    
    paginator = Paginator(blogs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    blog_categories = BlogCategory.objects.order_by('-created_at')
    featured_blogs = Blog.objects.filter(
        is_feature=True, 
        is_active=True
    ).order_by('-created_at')[:4]
    
    return render(request, 'blog/blog_index.html', {
        'page_obj': page_obj,
        'blog_categories': blog_categories,
        'current_category': category_slug,
        'featured_blogs': featured_blogs
    })

def blog_detail(request):
    return render(request, 'blog/blog_detail.html')
