
import re
from setuptools import setup

rgx = re.compile('([\w-]+==[\d.]+)')


def read_file(filename):
    """read file correctly."""
    with open(filename) as _file:
        return _file.read().strip()


def requirements(filename):
    """parse requirements from file."""
    return re.findall(rgx, read_file(filename)) or []


setup(name='libsasscompiler',
      version='0.1.5',
      description='django pipeline scss/sass compiler, no needed of ruby',
      url='https://github.com/sonic182/libsasscompiler',
      author='Johanderson Mogollon',
      author_email='johanderson@mogollon.com.ve',
      license='MIT',
      packages=['libsasscompiler'],
      setup_requires=['pytest-runner'],
      test_requires=['pytest'],
      install_requires=requirements('requirements.txt'),
      extras_require={
          'test': [
              'pytest<=3.2.0',
              'pytest-pep8<=1.8.0',
              'pytest-cov<=2.6.0',
              'django<=1.12.0',
              'coveralls',
              'django-pipeline<=1.7.0'
          ]
      },
      zip_safe=False)
