#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

install_requires = [
    'oauth2client<2.0.0',
    'bigquery-python',
]

tests_require = [
    'mock',
]

setup(
    name='izberg-bigquery-python',
    version='0.3.1',
    description='Python client for Google BigQuery.',
    long_description=readme + '\n\n' + history,
    author='Antoine Cezar',
    author_email='antoine@izberg-marketplace.com',
    url='https://github.com/izberg-marketplace/izberg-bigquery-python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license='ISCL',
    zip_safe=False,
    keywords='bigquery',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=tests_require
)
