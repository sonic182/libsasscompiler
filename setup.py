
import re
from setuptools import setup


def version():
    data = read_file('./libsasscompiler/version.py')
    return re.findall(r"VERSION = '([a-z0-9.]*)'", data)[0]


rgx = re.compile('([\w-]+[<=]{1}=[\d.]+)')


def read_file(filename):
    """read file correctly."""
    with open(filename) as _file:
        return _file.read().strip()


def requirements(filename):
    """parse requirements from file."""
    return re.findall(rgx, read_file(filename)) or []


setup(name='libsasscompiler',
      version=version(),
      python_requires='>=3.6.0',
      description='django pipeline scss/sass compiler, no needed of ruby',
      url='https://github.com/sonic182/libsasscompiler',
      long_description=read_file('README.md'),
      long_description_content_type='text/markdown',
      author='Johanderson Mogollon',
      author_email='johanderson@mogollon.com.ve',
      license='MIT',
      packages=['libsasscompiler'],
      setup_requires=[],
      test_requires=['pytest'],
      install_requires=requirements('requirements.txt'),
      extras_require={
          'test': requirements('test-requirements.txt')
      },
      zip_safe=False)
