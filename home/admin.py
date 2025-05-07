from django.contrib import admin
from core.wagtail_hooks import *
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import *
from wagtail.images.models import Image
from wagtail.admin.viewsets.model import ModelViewSet


class CarouselAdmin(SnippetViewSet):
    model = Carousel
    menu_label = "Carousel"
    icon = "home"
    list_display = [
        "top_text",
        "bottom_text",
        ImageColumn("image_1200x630", label="Image"),
        "link_text",
        "link",
    ]
    search_fields = ["top_text", "bottom_text", "link", "link_text"]
    list_filter = ["top_text", "bottom_text", "link", "link_text"]


class ClinetCarouselAdmin(SnippetViewSet):
    model = ClientCarousel
    menu_label = "Client Carousel"
    icon = "home"
    list_display = [
        "client_name",
        ImageColumn("image_50x50", label="Image"),
    ]
    search_fields = ["client_name"]
    list_filter = ["client_name"]

class CorrugatedBoardThicknessAdmin(SnippetViewSet):
    model = CorrugatedBoardThickness
    menu_label = "Corrugated Board Thickness"
    icon = "home"
    list_display = [
        "title",
        ImageColumn("image_600x400", label="Image"),
    ]
    search_fields = ["title"]
    list_filter = ["title"]

class OurServicesAdmin(SnippetViewSet):
    model = OurServices
    menu_label = "Our Services"
    icon = "home"
    list_display = [
        "title",
        ImageColumn("image_50x50", label="Image"),
    ]
    search_fields = ["title"]
    list_filter = ["title"]

class HomeSnippedAdmin(SnippetViewSetGroup):
    menu_label = "Home"
    menu_icon = "home"
    menu_order = 1
    items = (CarouselAdmin, ClinetCarouselAdmin, CorrugatedBoardThicknessAdmin, OurServicesAdmin)


register_snippet(HomeSnippedAdmin)
