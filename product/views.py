from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from contact_us.views import ContactForm
from contact_us.models import ContactUs
from .models import Product, ProductCategory
import user_agents

from django.core.paginator import Paginator

def product_index(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    
    # Prefetch related images to avoid N+1 queries
    products = Product.objects.all().prefetch_related('images')
    
    if search_query:
        products = products.filter(title__icontains=search_query)
    
    if category_id:
        products = products.filter(product_category__id=category_id)
    
    # Prepare products with template-expected fields
    product_list = []
    for product in products:
        first_image = product.images.first()  # Get first image or None if no images
        
        product_data = {
            'title': product.title,
            'slug': product.slug,
            'description': product.description,
            'category': product.product_category.name if product.product_category else '',
            'image': first_image.image_320x240_processed.url if first_image else 'https://placehold.co/320x240',
        }
        product_list.append(product_data)
    
    paginator = Paginator(product_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = ProductCategory.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    }
    
    return render(request, 'product/product_index.html', context)


def product_detail(request, product_slug=None):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # Check if user submitted too recently
        ip = request.META.get('REMOTE_ADDR')
        last_submit = ContactUs.objects.filter(ip_address=ip).order_by('-last_submit').first()
        
        if last_submit and (timezone.now() - last_submit.last_submit).total_seconds() < 300:
            messages.error(request, 'Anda hanya dapat mengirim pesan setiap 5 menit')
            return redirect('product:product_detail', product_slug=product_slug)
            
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Get user info
            ip = request.META.get('REMOTE_ADDR')
            user_agent_str = request.META.get('HTTP_USER_AGENT', '')
            user_agent = user_agents.parse(user_agent_str)
            
            # Save to database
            ContactUs.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
                ip_address=ip,
                user_agent=user_agent_str,
                last_submit=timezone.now()
            )

            messages.success(request, 'Pesan telah terkirim')
            return redirect('product:product_detail', product_slug=product_slug)
        else:
            messages.error(request, 'Terdapat kesalahan dalam form, silakan coba lagi')
            return redirect('product:product_detail', product_slug=product_slug)
    
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product': product,
        'form': form,
        'specifications': product.specifications.all(),
        'images': product.images.all(),
        'related_products': Product.objects.filter(
            product_category=product.product_category
        ).exclude(id=product.id)[:3]
    }
    return render(request, 'product/product_detail.html', context)
