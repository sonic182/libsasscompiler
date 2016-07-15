import codecs
import sass
from pipeline.compilers import CompilerBase


class LibSassCompiler(CompilerBase):
  output_extension = 'css'

  def match_file(self, filename):
    return filename.endswith('.scss')

  def compile_file(self, infile, outfile, outdated=False, force=False):
    f = codecs.open(outfile, 'w', 'utf-8')
    f.write(sass.compile(filename=infile))
    return f.close()
