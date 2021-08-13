#!/usr/bin/env python
# coding=utf-8
import os
from setuptools import setup, find_packages

if os.path.exists("requirements.txt"):
    install_requires = open("requirements.txt").read().split("\n")
else:
    install_requires = []

setup(
    name='wencai',
    version='0.2.5',
    author='allen yang',
    author_email='allenyzx@163.com',
    url='https://upload.pypi.org/allenyzx/',
    description='this is a wencai crawler to get message',
    packages=find_packages(),
    install_requires=install_requires,
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.5",
    ],
    zip_safe=False,
    include_package_data=True,

)
