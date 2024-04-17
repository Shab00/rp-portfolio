# pages/urls.py

from django.urls import path 

from pages import views

from django.contrib import admin


urlpatterns = [
    path("", views.home, name='home'),
    path("pages/templates/pages/contact", views.contact, name='contact'),
    path("pages/templates/pages/about", views.about, name='about'),
    path("static", views.download, name="static"),
]

