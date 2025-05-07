from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_index, name='product_index'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail'),
]
