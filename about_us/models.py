from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from wagtail.admin.panels import FieldPanel
from solo.models import SingletonModel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

# Create your models here.
# @register_setting
# @register_setting
class AboutUs(BaseGenericSetting):
    main_text = models.CharField(null=True, blank=True, max_length=255)
    small_text = models.CharField(null=True, blank=True, max_length=255)
    video_url = models.URLField(null=True, blank=True, max_length=255)
    video_background_555x423 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    video_background_555x423_processed = ImageSpecField(
        source="video_background_555x423",
        processors=[ResizeToFill(555 , 423)],
        format="webP",
        options={"quality": 90},
    )

    text_1 = models.CharField(null=True, blank=True, max_length=255)
    text_small_1 = models.CharField(null=True, blank=True, max_length=255)
    text_icon_35x35_1 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    text_icon_35x35_1_processed = ImageSpecField(
        source="text_icon_35x35_1",
        processors=[ResizeToFill(35 , 35)],
        format="webP",
        options={"quality": 90},
    )
    text_2 = models.CharField(null=True, blank=True, max_length=255)
    text_small_2 = models.CharField(null=True, blank=True, max_length=255)
    text_icon_35x35_2 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    text_icon_35x35_2_processed = ImageSpecField(
        source="text_icon_35x35_2",
        processors=[ResizeToFill(35 , 35)],
        format="webP",
        options={"quality": 90},
    )
    text_3 = models.CharField(null=True, blank=True, max_length=255)
    text_small_3 = models.CharField(null=True, blank=True, max_length=255)
    text_icon_35x35_3 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    text_icon_35x35_3_processed = ImageSpecField(
        source="text_icon_35x35_3",
        processors=[ResizeToFill(35 , 35)],
        format="webP",
        options={"quality": 90},
    )
    text_4 = models.CharField(null=True, blank=True, max_length=255)
    text_small_4 = models.CharField(null=True, blank=True, max_length=255)
    text_icon_35x35_4 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    text_icon_35x35_4_processed = ImageSpecField(
        source="text_icon_35x35_4",
        processors=[ResizeToFill(35 , 35)],
        format="webP",
        options={"quality": 90},
    )
    
    panels = [
        FieldPanel("main_text"),
        FieldPanel("small_text"),
        FieldPanel("video_url"),
        FieldPanel("video_background_555x423"),
        FieldPanel("text_1"),
        FieldPanel("text_small_1"),
        FieldPanel("text_icon_35x35_1"),
        FieldPanel("text_2"),
        FieldPanel("text_small_2"),
        FieldPanel("text_icon_35x35_2"),
        FieldPanel("text_3"),
        FieldPanel("text_small_3"),
        FieldPanel("text_icon_35x35_3"),
        FieldPanel("text_4"),
        FieldPanel("text_small_4"),
        FieldPanel("text_icon_35x35_4"),
    ]

    class Meta:
        verbose_name = "About Us Settings"

class TeamSupport(BaseGenericSetting):
    tim_support_190x190 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    tim_support_190x190_processed = ImageSpecField(
        source="tim_support_190x190",
        processors=[ResizeToFill(190 , 190)],
        format="webP",
        options={"quality": 90},
    )
    tim_support_name = models.CharField(null=True, blank=True, max_length=255)
    tim_support_wa = models.CharField(null=True, blank=True, max_length=255)
    tim_support_link = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "Team Support (Max 3)"


def limit_team_support_instances(sender, instance, **kwargs):
    if not instance.pk and TeamSupport.objects.count() >= 3:
        raise ValidationError("Anda hanya bisa membuat maksimal 3 instance Team Support")

pre_save.connect(limit_team_support_instances, sender=TeamSupport)



class Testimonial(models.Model):
    client_image_100x100 = models.ImageField(upload_to='about_us', blank=False, null=False , default="")
    client_image_100x100_processed = ImageSpecField(
        source="client_image_100x100",
        processors=[ResizeToFill(100 , 100)],
        format="webP",
        options={"quality": 90},
    )
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100)
    client_description = models.TextField()
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.client_name} - {self.client_role}"
