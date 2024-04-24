import os

from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def contact(request):
    if request.method == 'POST':
    
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            html = render_to_string('pages/emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            send_mail('You have a new message!', 'This is the message', 'noreply@bashaardhoot.com', ['bashaardhoot@gmail.com'], html_message=html)

            return redirect('contact')
    else:
        form = ContactForm()


    return render(request, "pages/contact.html", {
        'form': form
    })

def about(request):
    return render(request, "pages/about.html", {})

def download(request):
    file = os.path.join(settings.BASE_DIR, 'static/BashaarCV.rtf')

    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)
