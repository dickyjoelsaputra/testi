from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.http import JsonResponse


def blog_index(request, category_slug=None):
    blogs = Blog.objects.filter(is_active=True).order_by('-created_at')
    
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        blogs = blogs.filter(categories=category)
    
    paginator = Paginator(blogs, 5)
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

def blog_detail(request, blog_slug=None):
    blog = get_object_or_404(Blog, slug=blog_slug, is_active=True)
    
    # Get related blogs (same categories, excluding current blog)
    related_blogs = Blog.objects.filter(
        categories__in=blog.categories.all(),
        is_active=True
    ).exclude(id=blog.id).distinct().order_by('-created_at')[:3]
    
    # Get previous and next blogs
    previous_blog = Blog.objects.filter(
        created_at__lt=blog.created_at,
        is_active=True
    ).order_by('-created_at').first()
    
    next_blog = Blog.objects.filter(
        created_at__gt=blog.created_at,
        is_active=True
    ).order_by('created_at').first()
    
    return render(request, 'blog/blog_detail.html', {
        'blog': blog,
        'related_blogs': related_blogs,
        'previous_blog': previous_blog,
        'next_blog': next_blog
    })
