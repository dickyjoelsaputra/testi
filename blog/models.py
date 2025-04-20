from django.db import models
from django import forms
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
    image = models.ImageField(upload_to='media/blog/image', blank=False, null=False)
    
    image_processed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(640)],
        format="webP",
        options={"quality": 90},
    )

    content = StreamField(
        [
            (
                "paragraph",
                blocks.RichTextBlock(features=["p", "a"]),
            ),
            (
                "h4",
                blocks.CharBlock(features=["h4"]),
            ),
            (
                "h6",
                blocks.CharBlock(features=["h6"]),
            ),
            (
                "ordered_list",
                blocks.RichTextBlock(
                    features=["ol"],
                ),
            ),
            (
                "unordered_list",
                blocks.RichTextBlock(
                    features=["ul"],
                ),
            ),
            ("blockquote_1", blocks.CharBlock()),
            (
                "image",
                ImageChooserBlock(label="Image", help_text="800 x 600"),
            ),
        ],
        use_json_field=True,
        null=True,
        blank=True,
    )
    
    # seo
    meta_key = models.TextField(max_length=250, blank=True, null=True) #ok
    meta_desc = models.TextField(max_length=250, blank=True, null=True) #ok
    
    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    search_fields = [
        index.SearchField("title"),
    ]

    panels = [
        FieldPanel("title"),
        FieldPanel("author"),
        FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
        FieldPanel("image"),
        FieldPanel("content"),
        FieldPanel("meta_key"),
        FieldPanel("meta_desc"),
    ]
    
    search_fields = [
        index.SearchField("title"),
        index.SearchField("author"),
        index.SearchField("categories"),
        index.SearchField("content"),
    ]
    
    def __str__(self):
        return self.title
