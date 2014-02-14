#! /usr/bin/env python
from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(name='bare-bones',
      version='0.0',
      author='Enthought Inc.',
      description='A skeleton Tasks/Envisage application',
      long_description=long_description,
      author_email='xxx@enthought.com',
      url='',  # TODO Update this
      requires=['envisage'],
      py_modules=['bare_bones'],
      entry_points={
          'console_scripts': [
              'bare_bones_app = bare_bones.run:main',
          ],
      })
