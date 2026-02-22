"""Libsass compiler for django-pipeline.

Speedups development and/or production when compiling sass assets. No need of
ruby sass anymore.
"""

import sass
import codecs
import os
from pipeline.compilers import CompilerBase
from django.conf import settings


class LibSassCompiler(CompilerBase):
    """Compiler that uses libsass."""

    output_extension = 'css'

    def match_file(self, filename):
        """Check files extension to use them."""
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, infile, outfile, outdated=False, force=False):
        """Process sass file."""
        myfile = codecs.open(outfile, 'w', 'utf-8')

        include_paths = [os.path.dirname(infile)]
        include_paths.extend(getattr(settings,
                                     'LIBSASSCOMPILER_INCLUDE_PATHS',
                                     []))
        compile_kwargs = {
            'filename': infile,
            'include_paths': include_paths,
        }

        if settings.DEBUG:
            myfile.write(sass.compile(**compile_kwargs))
        else:
            compile_kwargs['output_style'] = 'compressed'
            myfile.write(sass.compile(**compile_kwargs))
        return myfile.close()
