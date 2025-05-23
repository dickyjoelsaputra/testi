from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from blog import views as blog_views
# from views import *
from core.views import custom_404_view, custom_500_view
from django.conf.urls import handler404, handler500
# from global_setting import views as global_views

handler404 = custom_404_view
handler500 = custom_500_view

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    
    # path("select2/", include("django_select2.urls")),
    
    path("", include('home.urls')),
    path("blog/", include('blog.urls')),
    path("contact_us/", include('contact_us.urls')),
    path("about_us/" , include('about_us.urls')),
    path("product/", include('product.urls')),
    
    # chapta
    path('captcha/', include('captcha.urls')),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
