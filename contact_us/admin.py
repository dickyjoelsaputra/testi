from django.contrib import admin
from core.wagtail_hooks import *
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import (
    ContactUs,FAQ
)

from wagtail.images.models import Image
from wagtail.admin.viewsets.model import ModelViewSet

class FAQAdmin(SnippetViewSet):
    model = FAQ
    menu_label = "FAQs"
    icon = "mail"
    list_display = ["question", "answer", "order"]
    # list_editable = ["order"]

class ContactUsAdmin(SnippetViewSet):
    model = ContactUs
    menu_label = "Contact Us"
    menu_icon = "mail"
    icon = "tag"
    list_display = ('name', 'email', 'phone', 'message', 'ip_address', 'location')
    search_fields = ('name', 'email', 'phone', 'message', 'ip_address', 'location')
    list_filter = ('name', 'email', 'phone', 'message', 'ip_address', 'location')
    list_per_page = 30
    # add_to_admin_menu = True

class ContactUsSnippedAdmin(SnippetViewSetGroup):
    menu_label = "Contact Us"
    menu_icon = "mail"
    menu_order = 4
    items = (ContactUsAdmin, FAQAdmin)
    
register_snippet(ContactUsSnippedAdmin)