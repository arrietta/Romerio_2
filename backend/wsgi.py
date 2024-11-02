"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# import os
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
#
# application = get_wsgi_application()

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u0000006/data/www/romerio.ru/Romerio')
sys.path.insert(1, '/var/www/u0000006/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
application = get_wsgi_application()