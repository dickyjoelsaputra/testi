from django.db import models
from wagtail.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel
from autoslug import AutoSlugField
from wagtail.snippets.models import register_snippet
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

# Create your models here.
class ProductCategory(index.Indexed,models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(max_length=255,populate_from="name")
    image_376x376 = models.ImageField(upload_to='product', blank=False, null=False , default="")
    image_376x376_processed = ImageSpecField(
        source="image_376x376",
        processors=[ResizeToFill(376 , 376)],
        format="webP",
        options={"quality": 90},
    )
    is_featured = models.BooleanField(default=False)
    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    search_fields = [
        index.SearchField("name"),
        index.SearchField("is_featured"),
    ]
    
    panels = [
        FieldPanel("name"),
        FieldPanel("is_featured"),
        FieldPanel("image_376x376"),
    ]
    
    def __str__(self):
        return self.name

# @register_snippet
class ProductSpecification(models.Model):
    product = ParentalKey('Product', on_delete=models.CASCADE, related_name='specifications')
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    panels = [
        FieldPanel("key"),
        FieldPanel("value"),
    ]
    
    def __str__(self):
        return f"{self.key}: {self.value}"
    
    class Meta:
        ordering = ['key']

# @register_snippet
class ProductImage(models.Model):
    product = ParentalKey('Product', on_delete=models.CASCADE, related_name='images')
    image_320x240 = models.ImageField(upload_to='product_images/')
    image_320x240_processed = ImageSpecField(
        source='image_320x240',
        processors=[ResizeToFill(320, 240)],
        format='webP',
        options={'quality': 90}
    )


    panels = [
        FieldPanel("image_320x240"),
    ]
    
    def __str__(self):
        return f"Image for {self.product.title}"
    
    class Meta:
        ordering = ['id']

class Product(index.Indexed, ClusterableModel):
    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title')
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    is_featured = models.BooleanField(default=False)
    description = models.TextField()
    content = RichTextField()
    meta_key = models.CharField(max_length=255, blank=True)
    meta_desc = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    search_fields = [
        index.SearchField('title'),
        index.SearchField('description'),
        index.SearchField('content'),
        index.SearchField('meta_key'),
        index.SearchField('meta_desc'),
        index.SearchField('is_featured'), 
    ]

    panels = [
        FieldPanel('title'),
        FieldPanel('is_featured'),
        FieldPanel('product_category'),
        FieldPanel('description'),
        FieldPanel('content'),
        FieldPanel('meta_key'),
        FieldPanel('meta_desc'),
        InlinePanel('specifications', heading="Specifications", label="Add Specification"),
        InlinePanel('images', heading="Images", label="Add Image"),
    ]

    def __str__(self):
        return self.title
