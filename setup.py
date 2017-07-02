from setuptools import setup


setup(name='libsasscompiler',
      version='0.1.3',
      description='django pipeline scss/sass compiler, no needed of ruby',
      url='https://github.com/sonic182/libsasscompiler',
      author='Johanderson Mogollon',
      author_email='johanderson@mogollon.com.ve',
      license='MIT',
      packages=['libsasscompiler'],
      install_requires=[
          'libsass',
          'django-pipeline'
      ],
      extras_require={
          'test': [
              'pytest',
              'pytest-pep8',
              'pytest-cov',
              'django',
              'django-pipeline'
          ]
      },
      zip_safe=False)
