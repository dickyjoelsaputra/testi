from django.urls import path

from . import views

app_name = "contact_us"

urlpatterns = [
    path('', views.contact_us_index, name='contact_us_index'),
]
