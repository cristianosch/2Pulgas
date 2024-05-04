from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    text = AboutUs.objects.all()
    context = {
        'text':text
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')
