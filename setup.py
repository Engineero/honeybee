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
 
CLASSIFIERS = ['Development Status :: 2 - Pre-Alpha',
               'Environment :: Console',
               'Intended Audience :: Developers',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Topic :: Scientific/Engineering',
               'Topic :: Scientific/Engineering :: Artificial Intelligence',
               'Topic :: Scientific/Engineering :: Artificial Life',
               'Topic :: Utilities']
PROJECT_URLS = {'Documentation': 'https://engineero.github.io/honeybee',
                'Source': 'https://github.com/Engineero/honeybee',
                'Tracker': 'https://github.com/Engineero/honeybee/issues'}
INSTALL_REQUIRES = ['numpy']

setup(name='honeybee',
      packages=['honeybee'],
      version=version_dict['__version__'],
      description='An artificial bee colony implementation in Python',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Engineero',
      author_email='engineerolabs@gmail.com',
      url='https://github.com/Engineero/honeybee',
      project_urls=PROJECT_URLS,
      keywords=['abc artificial bee colony optimization'],
      classifiers=CLASSIFIERS,
      install_requires=INSTALL_REQUIRES)
