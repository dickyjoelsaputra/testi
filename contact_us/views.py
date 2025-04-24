from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from contact_us.models import ContactUs
from django.conf import settings
from captcha.fields import CaptchaField
from django import forms
import geoip2.database
import user_agents

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nama'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Nomer Telepon'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Pesan'}))
    captcha = CaptchaField()

def contact_us_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        # Check if user submitted too recently
        ip = request.META.get('REMOTE_ADDR')
        last_submit = ContactUs.objects.filter(ip_address=ip).order_by('-last_submit').first()
        
        if last_submit and (timezone.now() - last_submit.last_submit).total_seconds() < 300:
            messages.error(request, 'Anda hanya dapat mengirim pesan setiap 5 menit')
            return redirect('contact_us:contact_us_index')
            
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Get user info
            ip = request.META.get('REMOTE_ADDR')
            user_agent_str = request.META.get('HTTP_USER_AGENT', '')
            user_agent = user_agents.parse(user_agent_str)
            
            # Get location from IP
            location = 'Unknown'
            try:
                with geoip2.database.Reader('GeoLite2-City.mmdb') as reader:
                    response = reader.city(ip)
                    location = f"{response.city.name}, {response.country.name}"
            except:
                pass

            # Save to database
            contact = ContactUs.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
                ip_address=ip,
                user_agent=user_agent_str,
                location=location,
                last_submit=timezone.now()
            )

            # Send email notification with additional info
            # email_subject = f'New Contact Form Submission from {name}'
            # email_message = f'''
            # Name: {name}
            # Email: {email}
            # Phone: {phone}
            # Message: {message}
            
            # Additional Info:
            # IP Address: {ip}
            # Location: {location}
            # Device: {user_agent.device.family}
            # Browser: {user_agent.browser.family} {user_agent.browser.version_string}
            # OS: {user_agent.os.family} {user_agent.os.version_string}
            # '''
            
            # send_mail(
            #     email_subject,
            #     email_message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     ['dickyjoelsaputra@gmail.com'],
            #     fail_silently=False,
            # )

            messages.success(request, 'Pesan telah terkirim')
            return redirect('contact_us:contact_us_index')
        else:
            messages.error(request, 'Terdapat kesalahan dalam form, silakan coba lagi')
            return redirect('contact_us:contact_us_index')
    
    form = ContactForm()
    return render(request, 'contact_us/contact_us_index.html', {'form': form})
