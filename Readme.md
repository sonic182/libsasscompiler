# Libsasscompiler

A fast scss/sass compiler for [django-pipeline](https://github.com/jazzband/django-pipeline)

# Install

`pip install libsasscompiler`

# Usage

Add to your pipeline compiler 
```
PIPELINE['COMPILERS'] = (
  'libsasscompiler.LibSassCompiler',
)
```
