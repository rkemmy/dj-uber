"""
WSGI config for Cuber project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
from whitenoise.django import DjangoWhiteNoise
=======
>>>>>>> f143df790f8dda548ddd5db501226561c672b338

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cuber.settings")

application = get_wsgi_application()
<<<<<<< HEAD

application = DjangoWhiteNoise(application)

=======
>>>>>>> f143df790f8dda548ddd5db501226561c672b338
