from django.shortcuts import render
from .models import AboutUs
from blog.utils import get_quote


def about_us(request):
    text = AboutUs.objects.all()
    quote = get_quote()
    context = {
        'text':text,
        'quote': quote,
    }
    return render(request, 'about.html', context)


def contact(request):
    return render(request, 'contact.html')
