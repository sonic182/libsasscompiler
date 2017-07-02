
[![Build Status](https://travis-ci.org/sonic182/libsasscompiler.svg?branch=master)](https://travis-ci.org/sonic182/libsasscompiler)
[![Coverage Status](https://coveralls.io/repos/github/sonic182/libsasscompiler/badge.svg?branch=master)](https://coveralls.io/github/sonic182/libsasscompiler?branch=master)

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

# Contribute

1. Fork
2. create a branch `feature/your_feature`
3. commit - push - pull request

Thanks :)
