from django.contrib import admin
from core.wagtail_hooks import *
from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import *
from wagtail.images.models import Image

class AboustUsAdmin(SnippetViewSet):
    model = AboutUs
    menu_label = "About Us"
    icon = "image"
    list_display = [
        "main_text",
        "small_text",
        ImageColumn("video_background_555x423", label="Video Background"),
        "text_1",
        "text_small_1",
        ImageColumn("text_icon_35x35_1", label="Text Icon 1"),
        "text_2",
        "text_small_2",
        ImageColumn("text_icon_35x35_2", label="Text Icon 2"),
        "text_3",
        "text_small_3",
        ImageColumn("text_icon_35x35_3", label="Text Icon 3"),
        "text_4",
        "text_small_4",
        ImageColumn("text_icon_35x35_4", label="Text Icon 4"),
    ]


class TeamSupportAdmin(SnippetViewSet):
    model = TeamSupport
    menu_label = "Team Support"
    icon = "globe"
    list_display = [
        "tim_support_name",
        "tim_support_wa",
        ImageColumn("tim_support_190x190", label="tim_support_190x190"),
    ]


class TestimonialAdmin(SnippetViewSet):
    model = Testimonial
    menu_label = "Testimonials" 
    icon = "globe"
    list_display = [
        "client_name",
        "client_role",
        ImageColumn("client_image_100x100", label="Client Image"),
    ]

class AboutUsSnippedAdmin(SnippetViewSetGroup):
    menu_label = "About Us"
    menu_icon = "globe"
    menu_order = 3
    items = (TeamSupportAdmin, TestimonialAdmin)
    

register_snippet(AboutUsSnippedAdmin)
