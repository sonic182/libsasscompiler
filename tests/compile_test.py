"""Tests."""

import os
import sass
import django

from django.core.management import call_command
from django.conf import settings

# Make collectstatic command work.
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "test_djangoapp.django_app.settings")
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


def test_import_from_django_app_static_dir():
    """Import should work for files in app static dirs."""
    from libsasscompiler import LibSassCompiler

    previous_paths = getattr(settings, 'LIBSASSCOMPILER_INCLUDE_PATHS', None)
    settings.LIBSASSCOMPILER_INCLUDE_PATHS = [
        os.path.join(settings.BASE_DIR, 'django_app', 'static')
    ]

    compiler = LibSassCompiler(verbose=False, storage=None)
    infile = os.path.join(settings.STATICFILES_DIRS[0], 'tests/import_main.scss')
    outfile = os.path.join(settings.STATIC_ROOT, 'css/import_main.css')

    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    try:
        compiler.compile_file(infile, outfile)
    finally:
        if previous_paths is None:
            delattr(settings, 'LIBSASSCOMPILER_INCLUDE_PATHS')
        else:
            settings.LIBSASSCOMPILER_INCLUDE_PATHS = previous_paths

    with open(outfile) as compiled:
        css = compiled.read()

    assert 'color:red' in css.replace(' ', '')
