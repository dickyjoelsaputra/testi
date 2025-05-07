from django.shortcuts import render
from .models import AboutUs, TeamSupport, Testimonial


def about_us_index(request):
    about = AboutUs.load()
    team_supports = TeamSupport.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    context = {
        'about': about,
        'team_supports': team_supports,
        'testimonials': testimonials,
    }
    return render(request, "about_us/about_us_index.html", context)
