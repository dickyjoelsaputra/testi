from django.db import models
from django import forms
from modelcluster.fields import ParentalManyToManyField
from django_select2 import forms as s2forms
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from autoslug import AutoSlugField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

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
    
class Blog(index.Indexed , models.Model):
    title = models.CharField(max_length=200, blank=False , unique=True)
    slug = AutoSlugField(populate_from="title", blank=True, null=True)
    author = models.CharField(max_length=30, blank=False , null=False , default="")
    categories = models.ManyToManyField(BlogCategory, blank=True)
    is_feature = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    image_330x220 = models.ImageField(upload_to='media/blog/image', blank=False, null=False, default="")
    image_330x220_processed = ImageSpecField(
        source="image_330x220",
        processors=[ResizeToFill(330 , 220)],
        format="webP",
        options={"quality": 90},
    )
    image_240x160_processed = ImageSpecField(
        source="image_330x220",
        processors=[ResizeToFill(240 , 160)],
        format="webP",
        options={"quality": 90},
    )
    image_105x80_processed = ImageSpecField(
        source="image_330x220",
        processors=[ResizeToFill(105 , 80)],
        format="webP",
        options={"quality": 90},
    )


    image_1920x640 = models.ImageField(upload_to='media/blog/image', blank=False, null=False , default="")
    image_1920x640_processed = ImageSpecField(
        source="image_1920x640",
        processors=[ResizeToFill(1920 , 640)],
        format="webP",
        options={"quality": 90},
    )

    content = RichTextField(blank=True, null=True)
    small_content = models.TextField(max_length=200, blank=True)
    # seo
    meta_key = models.TextField(max_length=250, blank=True, null=True) #ok
    meta_desc = models.TextField(max_length=250, blank=True, null=True) #ok
    
    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    search_fields = [
        index.SearchField("title"),
        index.SearchField("author"),
        index.SearchField("categories"),
        index.SearchField("content"),
        index.SearchField("small_content"),
        index.SearchField("is_feature"),
    ]

    panels = [
        FieldPanel("title"),
        FieldPanel("author"),
        FieldPanel("categories",widget=s2forms.Select2MultipleWidget(attrs={
            "style": "width: 100%; min-height: 40px;"
        })),
        FieldPanel("image_330x220"),
        FieldPanel("image_1920x640"),
        FieldPanel("is_feature"),
        FieldPanel("is_active"),
        FieldPanel("content"),
        FieldPanel("small_content"),
        FieldPanel("meta_key"),
        FieldPanel("meta_desc"),
    ]
    
    def __str__(self):
        return self.title
