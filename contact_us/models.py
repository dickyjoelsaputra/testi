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
# Create your models here.
class ContactUs(index.Indexed, models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    search_fields = [
        index.SearchField("name"),
        index.SearchField("email"),
        index.SearchField("phone"),
        index.SearchField("message"),
    ]

    panels = [
        FieldPanel("name" , read_only=True),
        FieldPanel("email",read_only=True),
        FieldPanel("phone",read_only=True),
        FieldPanel("message",read_only=True),
    ]

    def __str__(self):
        return self.name