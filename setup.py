#! /usr/bin/env python
from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

setup(name='bare-bones',
      version='0.1',
      author='Enthought Inc.',
      description='A skeleton Tasks/Envisage application',
      long_description=long_description,
      author_email='xxx@enthought.com',
      url='',  # TODO Update this
      install_requires=[
        'envisage~=4.5',
        'traits~=4.6'
      ],
      packages=find_packages(),
      package_data={
          'bare_bones': ['preferences.ini'],
      },
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'bare_bones_app = bare_bones.run:main',
          ],
      })
