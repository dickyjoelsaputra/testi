from wagtail.admin.ui.tables import TitleColumn
from django.utils.safestring import mark_safe
from wagtail.admin.ui.tables import Column
from wagtail import hooks
from django.utils.html import format_html
from django.templatetags.static import static

# class ImageColumn(TitleColumn):
#     def get_cell_context_data(self, instance, parent_context):
#         context = super().get_cell_context_data(instance, parent_context)
#         # Gunakan URL dari ImageSpecField
#         try:
#             thumb_url = instance.image.url
#             context['value'] = mark_safe(
#                 f'<img src="{thumb_url}" style="max-height:200px;" />'
#             )
#         except Exception:
#             context['value'] = mark_safe(
#                 '<span class="icon icon-image">No image</span>'
#             )
#         return context

class ImageColumn(TitleColumn):
    def get_cell_context_data(self, instance, parent_context):
        context = super().get_cell_context_data(instance, parent_context)
        try:
            # Akses URL dari image processed
            thumb_url = getattr(instance, self.name).url
            context['value'] = mark_safe(
                f'<img src="{thumb_url}" style="max-height:100px;" />'
            )
        except Exception:
            context['value'] = mark_safe(
                '<span class="icon icon-image">No image</span>'
            )
        return context


class CategoriesColumn(Column):
    def get_value(self, instance):
        # Ambil semua kategori sebagai queryset, lalu gabung judulnya
        return ", ".join(cat.title for cat in instance.categories.all())

@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/admin.css")
    )