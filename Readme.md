# Libsasscompiler

A fast scss/sass compiler for [django-pipeline](https://github.com/jazzband/django-pipeline) using [python libsass port](https://github.com/dahlia/libsass-python) (no needed of ruby-sass anymore)

# Install

`pip install libsasscompiler`

# Usage

Add to your pipeline compiler
```
PIPELINE['COMPILERS'] = (
  'libsasscompiler.LibSassCompiler',
)
```
