"""
WSGI config for escout project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
# Import sys lib is required for apache launch

import os
import sys

sys.path.append("/var/www/escout-project/escout/service/back-end")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "escout.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
