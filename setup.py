#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = open('requirements.txt').read().splitlines()

test_requirements = open('requirements-test.txt').read().splitlines()

setup(
    name='izberg-bigquery-python',
    version='0.1.0',
    description="Python client for Google BigQuery.",
    long_description=readme + '\n\n' + history,
    author="Antoine Cezar",
    author_email='antoine@izberg-marketplace.com',
    url='https://github.com/izberg-marketplace/izberg-bigquery-python',
    packages=[
        'izberg_bigquery',
    ],
    package_dir={'izberg_bigquery':
                 'izberg_bigquery'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='bigquery',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
