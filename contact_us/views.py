from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from contact_us.models import ContactUs
from django.conf import settings

def contact_us_index(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to database
        contact = ContactUs.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Send email notification
        email_subject = f'New Contact Form Submission from {name}'
        email_message = f'''
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        '''
        
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            ['sales@eveza.id'],
            fail_silently=False,
        )

        return redirect('contact_us:contact_us_index')
    
    return render(request, 'contact_us/contact_us_index.html')
