# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2026-02-22

### Added
- Support `LIBSASSCOMPILER_INCLUDE_PATHS` setting to pass extra import search paths to `sass.compile(..., include_paths=...)`.

### Fixed
- SCSS imports can now resolve shared files outside the source file directory when custom include paths are configured.

## [0.2.0] - 2024-08-24
### Fixed
- Fix dependencies for working with django 2 (pending to update package so it works with django 3 and 4)

## [0.1.9] - 2021-11-02
### Fixed
- No pytest-runner in setup.py

## [0.1.8] - 2020-30-05
### Fixed
- Travis test image
- Python 3.5 not for travis test

## [0.1.7] - 2020-30-05
### Added
- Readme to pypi

## [0.1.6] - 2020-30-05
### Updated
- Support for django-pipeline<=2.1.0 and libsass 0.20.0
- Travis tests for python 3.6, 3.7 and 3.8
  - django-pipeline from version 2 drops support for Python<3.5 (including python2)

## [0.1.5] - 2017-09-10
### Added
- Tests and travis

## [0.1.4] - 2017-07-02
### Added
- Support of `.sass` files
- Changelog added
- Better handling if DEBUG

### Fixed
- Fixed indentation

[Unreleased]: https://github.com/sonic182/libsasscompiler/compare/0.2.1...master
[0.2.1]: https://github.com/sonic182/libsasscompiler/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/sonic182/libsasscompiler/compare/0.1.9...0.2.0
[0.1.9]: https://github.com/sonic182/libsasscompiler/compare/0.1.8...0.1.9
[0.1.8]: https://github.com/sonic182/libsasscompiler/compare/0.1.7...0.1.8
[0.1.7]: https://github.com/sonic182/libsasscompiler/compare/0.1.6...0.1.7
[0.1.6]: https://github.com/sonic182/libsasscompiler/compare/0.1.5...0.1.6
[0.1.5]: https://github.com/sonic182/libsasscompiler/compare/v0.1.4...0.1.5
[0.1.4]: https://github.com/sonic182/libsasscompiler/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/sonic182/libsasscompiler/compare/v0.1.2...v0.1.3
