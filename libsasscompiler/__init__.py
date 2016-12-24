import codecs
import sass
from pipeline.compilers import CompilerBase
from django.conf import settings

class LibSassCompiler(CompilerBase):
  output_extension = 'css'

  def match_file(self, filename):
    return filename.endswith('.scss')

  def compile_file(self, infile, outfile, outdated=False, force=False):
    f = codecs.open(outfile, 'w', 'utf-8')
    if settings.DEBUG:
        f.write(sass.compile(filename=infile))
    else:
        f.write(sass.compile(filename=infile, output_style='compressed'))
    return f.close()
