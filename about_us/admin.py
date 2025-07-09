from django.contrib import admin
from .models import AboutUs

# Register your models here.

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'description')
    