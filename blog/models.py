from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from autoslug import AutoSlugField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


class BlogCategory(index.Indexed, models.Model):
    title = models.CharField(max_length=30, blank=False , unique=True)
    slug = AutoSlugField(populate_from="title", blank=True, null=True)

    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    search_fields = [
        index.SearchField("title"),
    ]

    panels = [
        FieldPanel("title"),
    ]
    
    def __str__(self):
        return self.title