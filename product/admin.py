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
    icon = "image"
    menu_order = 200
    list_display = [
        "name",
        ImageColumn("image", label="Image"),
        "slug" 
    ]


class ProductSnippedAdmin(SnippetViewSetGroup):
    menu_label = "Product"
    icon = "image"
    menu_order = 200
    items = (ProductCategoryAdmin,)
    

register_snippet(ProductSnippedAdmin)