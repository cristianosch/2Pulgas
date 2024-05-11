from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django_resized import ResizedImageField




class AboutUs(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = ResizedImageField(size=[900, 400], force_format='PNG', upload_to='about_us/media/about', blank=True, null=True) 
    description = HTMLField() 