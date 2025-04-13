from django.shortcuts import render
from .models import *

def home_index(request):
    return render(request, 'home/home_index.html')
