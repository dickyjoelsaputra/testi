from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from .models import *
from wagtail.snippets.views.snippets import SnippetViewSet

# class BrandingSettingAdmin(SnippetViewSet):
#     model = BreadCrumb
#     menu_label = 'Breadcump' 
#     menu_icon = 'cog'
#     menu_order = 200
#     add_to_settings_menu = True  # Jika ingin muncul di Settings juga

# register_snippet(BrandingSettingAdmin)