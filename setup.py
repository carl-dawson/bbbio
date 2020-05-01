"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bbbio',
    version='0.0.1',
    description='basic I/O for the BeagleBone Black',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Carl Dawson',
    author_email='carl@carlsdawson.com',
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: BeagleBone Black Owners',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='BeagleBone',
    packages=find_packages(),
    install_requires=[],
    project_urls={
        'Bug Reports': '',
        'Source': '',
    },
)
