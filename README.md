
[![Build Status](https://travis-ci.org/sonic182/libsasscompiler.svg?branch=master)](https://travis-ci.org/sonic182/libsasscompiler)
[![Coverage Status](https://coveralls.io/repos/github/sonic182/libsasscompiler/badge.svg?branch=master)](https://coveralls.io/github/sonic182/libsasscompiler?branch=master)
[![PyPI version](https://badge.fury.io/py/libsasscompiler.svg)](https://badge.fury.io/py/libsasscompiler)

# Libsasscompiler

A fast scss/sass compiler for [django-pipeline](https://github.com/jazzband/django-pipeline) using [python libsass port](https://github.com/dahlia/libsass-python) (no needed of ruby-sass anymore)

# Requirements

Same as django-pipeline

# Install

`pip install libsasscompiler`

# Usage

Add to your pipeline compiler
```
PIPELINE['COMPILERS'] = (
  'libsasscompiler.LibSassCompiler',
)
```

Optional: add extra include paths for `@import` resolution.

```python
LIBSASSCOMPILER_INCLUDE_PATHS = [
    '/path/to/shared/styles',
    '/path/to/another/scss/dir',
]
```

These paths are passed to `sass.compile(..., include_paths=...)`.

Imports are resolved from:

1. the directory of the source scss/sass file
2. `LIBSASSCOMPILER_INCLUDE_PATHS` (if defined)

Example:

```scss
@import "shared";
```

With `LIBSASSCOMPILER_INCLUDE_PATHS = ['/path/to/shared/styles']`, libsass will resolve `/path/to/shared/styles/shared.scss`.

# Contribute

1. Fork
2. create a branch `feature/your_feature`
3. commit - push - pull request

Thanks :)
