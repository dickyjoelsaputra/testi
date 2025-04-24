from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from wagtail.search import index
from wagtail.admin.panels import FieldPanel
from autoslug import AutoSlugField

# Create your models here.
class ProductCategory(index.Indexed,models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(max_length=255,populate_from="name")
    image = models.ImageField(upload_to='product', blank=False, null=False , default="")
    image_processed = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1920 , 640)],
        format="webP",
        options={"quality": 90},
    )
    
    # date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    search_fields = [
        index.SearchField("name"),
    ]
    
    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
    ]

    
    def __str__(self):
        return self.name