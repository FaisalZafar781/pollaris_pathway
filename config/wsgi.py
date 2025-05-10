"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def create_superuser():
    import django
    django.setup()
    from django.contrib.auth import get_user_model

    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin12345")
        print("Superuser created")
    else:
        print("Superuser already exists")

create_superuser() 

application = get_wsgi_application()
