from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
