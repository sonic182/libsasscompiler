from setuptools import setup


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
      install_requires=[
          'libsass<=1.0.0',
          'django-pipeline<=1.7.0'
      ],
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
