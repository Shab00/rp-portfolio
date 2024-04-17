
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings 
import os

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def contact(request):
    return render(request, "pages/contact.html", {})

def about(request):
    return render(request, "pages/about.html", {})

def download(request):
    file = os.path.join(settings.BASE_DIR, 'static/BashaarCV.rtf')

    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)
