# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='zjzjzjzj1874@gmail.com',
    url='https://github.com/zjzjzjzj1874/py_tutorial',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)