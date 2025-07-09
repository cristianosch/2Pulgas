from django.test import TestCase

# Create your tests here.

import os
import django

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


from django.core.mail import send_mail
from django.conf import settings

def send_test_email():
    send_mail(
        'Test Email',
        'This is a test email.',
        settings.DEFAULT_FROM_EMAIL,
        ['cris85sch@gmail.com'],
        fail_silently=False,
    )

if __name__ == "__main__":
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    send_test_email()
