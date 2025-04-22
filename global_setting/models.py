from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from solo.models import SingletonModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust

@register_setting
class GlobalSEO(BaseGenericSetting):
    index_meta_key = models.CharField(blank=True, null=True)
    index_meta_desc = models.CharField(blank=True, null=True)
    produk_meta_key = models.CharField(blank=True, null=True)
    produk_meta_desc = models.CharField(blank=True, null=True)
    tentang_meta_key = models.CharField(blank=True, null=True)
    tentang_meta_desc = models.CharField(blank=True, null=True)
    kontak_meta_key = models.CharField(blank=True, null=True)
    kontak_meta_desc = models.CharField(blank=True, null=True)
    blog_meta_key = models.CharField(blank=True, null=True)
    blog_meta_desc = models.CharField(blank=True, null=True)

    panels = [
        FieldPanel("index_meta_key"),
        FieldPanel("index_meta_desc"),
        FieldPanel("produk_meta_key"),
        FieldPanel("produk_meta_desc"),
        FieldPanel("tentang_meta_key"),
        FieldPanel("tentang_meta_desc"),
        FieldPanel("kontak_meta_key"),
        FieldPanel("kontak_meta_desc"),
        FieldPanel("blog_meta_key"),
        FieldPanel("blog_meta_desc"),
    ]
    
    def __str__(self):
        return self.index_meta_key
