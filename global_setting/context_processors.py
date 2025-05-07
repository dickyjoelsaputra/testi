
from .models import *

def social_context(request):
    return {
        'social_context': Social.objects.first()
    }
    
def global_seo_context(request):
    return {
        'global_seo_context': GlobalSEO.objects.first()
    }
    
def breadcrump_context(request):
    return {
        'breadcrump_context': BreadCrumb.objects.first()
    }
    

def footer_text_context(request):
    return {
        'footer_text_context': FooterText.objects.first()
    }

def company_profile_context(request):
    return {
        'company_profile_context': CompanyProfile.objects.first()
    }