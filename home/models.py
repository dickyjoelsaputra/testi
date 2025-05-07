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


# class HomePage(Page):
#     pass

class ClientCarousel(models.Model):
    client_name = models.CharField(max_length=255)
    image_50x50 = models.ImageField(upload_to="client_carousel_images/50x50/")
    image_50x50_processed = ImageSpecField(
        source="image_50x50",
        processors=[ResizeToFill(100, 100)],
        format="webP",
        options={"quality": 90},
    )

    panels = [
        FieldPanel("client_name"),
        FieldPanel("image_50x50"),
    ]

    def __str__(self):
        return self.client_name

class Carousel(models.Model):
    top_text = models.CharField(max_length=255)
    bottom_text = models.CharField(max_length=255)
    image_1200x630 = models.ImageField(upload_to="carousel_images/1200x630/")
    image_1200x630_processed = ImageSpecField(
        source="image_1200x630",
        processors=[ResizeToFill(1200, 630)],
        format="webP",
        options={"quality": 90},
    )
    link_text = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("top_text"),
        FieldPanel("bottom_text"),
        FieldPanel("image_1200x630"),
        FieldPanel("link"),
        FieldPanel("link_text"),
    ]

    def __str__(self):
        return self.top_text


class OurServices(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_50x50 = models.ImageField(upload_to="our_services_images/50x50/")
    image_50x50_processed = ImageSpecField(
        source="image_50x50",
        processors=[ResizeToFill(50, 50)],
        format="webP",
        options={"quality": 90},
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("image_50x50"),
    ]

    def __str__(self):
        return self.title
    
class CorrugatedBoardThickness(models.Model):
    image_600x400 = models.ImageField(upload_to="corrugated_board_thickness_images/600x400/")
    image_600x400_processed = ImageSpecField(
        source="image_600x400",
        processors=[ResizeToFill(600, 400)],
        format="webP",
        options={"quality": 90},
    )
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
        FieldPanel("image_600x400"),
    ]

    def __str__(self):
        return self.title