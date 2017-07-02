"""Tests."""

import os
import sass
import django

from django.core.management import call_command
from django.conf import settings

# Make collectstatic command work.
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "django_app.django_app.settings")
django.setup()


def test_compress():
    """Test collectstatic command works."""
    call_command('collectstatic', verbosity=0, interactive=False)
    assert True


def test_asset_compilation():
    """Test scss file compilation."""
    call_command('collectstatic', verbosity=0, interactive=False)

    my_files = [{
        'normal': 'tests/test1.scss',
        'compiled': 'css/test_scss.css'
    }, {
        'normal': 'tests/test1.sass',
        'compiled': 'css/test_sass.css'
    }]

    for item in my_files:
        myfile = item['normal']
        myfile_compiled = item['compiled']

        staticdir_test = settings.STATICFILES_DIRS[0]
        static_path = settings.STATIC_ROOT

        file_compiled = sass.compile(filename=os.path.join(staticdir_test,
                                                           myfile))
        with open(os.path.join(static_path, myfile_compiled)) as _compiled:
            assert _compiled.read() == file_compiled
    assert True


def test_compilation_no_debug():
    settings.DEBUG = False
    django.setup()
    call_command('collectstatic', verbosity=0, interactive=False)
    assert True
