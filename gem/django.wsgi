import os
import sys

path='/var/www/PyGem/gem'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gem/gem.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()