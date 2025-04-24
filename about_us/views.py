from django.shortcuts import render

# Create your views here.
def about_us_index(request):
    return render(request, 'about_us/about_us_index.html')