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
class Social(BaseGenericSetting):
    alamat = models.CharField(max_length=200, blank=True, null=True)
    telepon = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    embed_map = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel("alamat"),
        FieldPanel("telepon"),
        FieldPanel("whatsapp"),
        FieldPanel("email"),
        FieldPanel("embed_map"),
    ]
    

@register_setting
class BreadCrumb(BaseGenericSetting):
    produk_breadcump_1920x348 = models.ImageField(upload_to='global_setting', blank=True, null=True)
    produk_breadcump_1920x348_processed = ImageSpecField(source='produk_breadcump_1920x348', processors=[ResizeToFill(1920, 348)], format='webP', options={'quality': 90})
    tentang_breadcump_1920x348 = models.ImageField(upload_to='global_setting', blank=True, null=True)
    tentang_breadcump_1920x348_processed = ImageSpecField(source='tentang_breadcump_1920x348', processors=[ResizeToFill(1920, 348)], format='webP', options={'quality': 90})
    kontak_breadcump_1920x348 = models.ImageField(upload_to='global_setting', blank=True, null=True)
    kontak_breadcump_1920x348_processed = ImageSpecField(source='kontak_breadcump_1920x348', processors=[ResizeToFill(1920, 348)], format='webP', options={'quality': 90})
    blog_breadcump_1920x348 = models.ImageField(upload_to='global_setting', blank=True, null=True)
    blog_breadcump_1920x348_processed = ImageSpecField(source='blog_breadcump_1920x348', processors=[ResizeToFill(1920, 348)], format='webP', options={'quality': 90})
    panels = [
        FieldPanel("produk_breadcump_1920x348"),
        FieldPanel("tentang_breadcump_1920x348"),
        FieldPanel("kontak_breadcump_1920x348"),
        FieldPanel("blog_breadcump_1920x348"),
    ]
    
    
    
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
    
    menu_label = "Global SEO"
    
@register_setting
class FooterText(BaseGenericSetting):
    footer_text = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel("footer_text"),
    ]
    
    menu_label = "Footer Text"

@register_setting
class CompanyProfile(BaseGenericSetting):
    company_alias = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_logo_69x42 = models.FileField(upload_to='global_setting', blank=True, null=True)
    # company_logo_69x42_processed = ImageSpecField(source='company_logo_69x42', processors=[ResizeToFill(69, 42)], format='webP', options={'quality': 90})
    company_logo_138x84 = models.FileField(upload_to='global_setting', blank=True, null=True)
    # company_logo_138x84_processed = ImageSpecField(source='company_logo_138x84', processors=[ResizeToFill(138, 84)], format='webP', options={'quality': 90})
    favicon_16x16 = models.FileField(upload_to='global_setting', blank=True, null=True)
    # favicon_16x16_processed = ImageSpecField(source='favicon_16x16', processors=[ResizeToFill(16, 16)], format='webP', options={'quality': 90})