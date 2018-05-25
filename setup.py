from setuptools import setup
from distutils.util import convert_path
from os import path


here = path.abspath(path.dirname(__file__))
version_dict = {}
version_path = convert_path('honeybee/_version.py')

# Get the version number from the version path.
with open(version_path, 'r') as ver_file:
    exec(ver_file.read(), version_dict)

# Get the long description from the README file.
with open(path.join(here, 'README.md')) as a_file:
    long_description = a_file.read()

setup(name='honeybee',
      version=version_dict['__version__'],
      description='An artificial bee colony implementation in Python',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Engineero')
