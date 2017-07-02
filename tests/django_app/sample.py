
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
django.setup()

from django.core.management import call_command

call_command('collectstatic', verbosity=0, interactive=False)
