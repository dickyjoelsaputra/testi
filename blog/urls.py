from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('category/<slug:category_slug>/', views.blog_index, name='blog_by_category'),
    path('detail/<slug:blog_slug>/', views.blog_detail, name='blog_detail'),
]
