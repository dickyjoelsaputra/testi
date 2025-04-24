from django.urls import path

from . import views

app_name = "about_us"

urlpatterns = [
    path('', views.about_us_index, name='about_us_index'),
]
