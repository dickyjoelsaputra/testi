from django.contrib import admin
from core.wagtail_hooks import *
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import (
    ContactUs
)

from wagtail.images.models import Image
from wagtail.admin.viewsets.model import ModelViewSet


class ContactUsAdmin(SnippetViewSet):
    model = ContactUs
    menu_label = "Contact Us"
    menu_icon = "mail"
    icon = "tag"
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone', 'message')
    list_filter = ('name', 'email', 'phone', 'message')
    list_per_page = 20
    add_to_admin_menu = True
    
register_snippet(ContactUsAdmin)