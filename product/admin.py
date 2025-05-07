from django.contrib import admin
from core.wagtail_hooks import *
from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import *
from wagtail.images.models import Image


class ProductCategoryAdmin(SnippetViewSet):
    model = ProductCategory
    menu_label = "Product Categories"
    icon = "media"
    menu_order = 200
    list_display = [
        "name",
        ImageColumn("image", label="Image"),
        "slug" 
    ]

class ProductAdmin(SnippetViewSet):
    model = Product
    menu_label = "Products"
    icon = "media"
    list_display = ["title", "product_category", "updated_at"]
    search_fields = ["title", "description", "content"]
    list_filter = ["product_category", "created_at"]
    ordering = ["-created_at"]
    panels = Product.panels
    
class ProductSnippedAdmin(SnippetViewSetGroup):
    menu_label = "Product"
    menu_icon = "media"
    menu_order = 2
    items = (ProductAdmin,ProductCategoryAdmin)
    

register_snippet(ProductSnippedAdmin)