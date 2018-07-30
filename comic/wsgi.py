"""
WSGI config for comic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

import sys
sys.path.append('/var/myproject/python/lib/python2.7/site-packages')
sys.path.append('/var/myproject/comic')

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comic.settings")
os.environ["DJANGO_SETTINGS_MODULE"] =  "comic.settings"

application = get_wsgi_application()
