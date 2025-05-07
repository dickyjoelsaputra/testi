from django.shortcuts import render
from .models import *
from about_us.models import AboutUs, TeamSupport, Testimonial
from product.models import ProductCategory, Product
from contact_us.models import FAQ

def home_index(request):
    # Fetch the carousel items from the database
    faqs = FAQ.objects.all().order_by('order')
    carousel_items = Carousel.objects.all()
    # Pass the carousel items to the template context
    our_services = OurServices.objects.all()
    testimonials = Testimonial.objects.all()
    clint_carousels = ClientCarousel.objects.all()
    # Get featured categories and their featured products
    featured_categories = ProductCategory.objects.filter(is_featured=True)[:5]

    featured_products = {}

    featured_products['all'] = Product.objects.order_by('-created_at').filter(is_featured=True)[:6]

    for category in featured_categories:
        featured_products[category.id] = Product.objects.order_by('-created_at').filter(
            product_category=category,
            is_featured=True,
        )[:6]

    class AllCategory:
        id = 'all'
        name = 'All'

    featured_categories = [AllCategory()] + list(featured_categories)

    # Get 6 featured categories with 3 featured products each
    fp_categories = ProductCategory.objects.filter(is_featured=True)[:6]
    fp_category_products = {}
    for category in fp_categories:
        fp_category_products[category.id] = Product.objects.filter(
            product_category=category,
            is_featured=True
        ).order_by('-created_at')[:3]

    corrugated_thickness = CorrugatedBoardThickness.objects.all()

    about = AboutUs.load()

    context = {
        'carousel_items': carousel_items,
        'our_services': our_services,
        'testimonials': testimonials,
        'clint_carousels': clint_carousels,
        'featured_categories': featured_categories,
        'featured_products': featured_products,
        'fp_categories': fp_categories,
        'fp_category_products': fp_category_products,
        'faqs': faqs,
        'corrugated_thickness': corrugated_thickness,
        'about': about,
    }
    return render(request, 'home/home_index.html', context)
