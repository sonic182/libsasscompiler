from pipeline.compilers import CompilerBase
import sass

class LibSassCompiler(CompilerBase):
  output_extension = 'css'

  def match_file(self, filename):
    return filename.endswith('.scss')

  def compile_file(self, infile, outfile, outdated=False, force=False):
    f = open(outfile, 'w')
    f.write(sass.compile(filename=infile))
    return f.close()
