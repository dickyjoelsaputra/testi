from django.contrib import admin
from core.wagtail_hooks import *

# Register your models here.

from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import (
    BlogCategory,
    Blog
)

from wagtail.images.models import Image

class BlogAdmin(SnippetViewSet):
    model = Blog
    menu_label = "Blog"
    icon = "edit"
    list_display = [
        "title",
        "author",
        CategoriesColumn("categories", label="Categories"),
        "is_feature",
        "is_active",
        ImageColumn("image_330x220", label="Image"),
    ]
    list_filter = ("is_feature", "is_active", "categories")
    search_fields = ["title", "author", "categories", "content", "small_content"]
    ordering = ["-created_at"]



class BlogCategoryAdmin(SnippetViewSet):
    model = BlogCategory
    menu_label = "Blog Categories"
    icon = "edit"
    list_display = ("title",)


class BlogSnippedAdmin(SnippetViewSetGroup):
    menu_icon = "edit"
    menu_label = "Blog"
    items = (
        BlogAdmin,
        BlogCategoryAdmin,
    )
    menu_order = 5
    
register_snippet(BlogSnippedAdmin)
