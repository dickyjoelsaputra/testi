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
    icon = "tag"
    menu_order = 20
    list_display = [
        "title",
        "author",
        CategoriesColumn("categories", label="Categories"),
        "is_feature",
        "is_active",
        ImageColumn("image", label="Image"),
    ]
    list_filter = ("is_feature", "is_active", "categories")

class BlogCategoryAdmin(SnippetViewSet):
    model = BlogCategory
    menu_label = "Blog Categories"
    icon = "tag"
    menu_order = 20
    list_display = ("title",)


class BlogSettingAdmin(SnippetViewSetGroup):
    menu_icon = "tag"
    menu_label = "Blog"
    menu_order = 20
    items = (
        BlogAdmin,
        BlogCategoryAdmin,
    )
    
register_snippet(BlogSettingAdmin)
