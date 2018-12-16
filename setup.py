#!/usr/bin/env python

import juc2

from setuptools import setup


setup(
    name='juc2',
    packages=['juc2', 'juc2.art'],
    version=juc2.__version__,
    description='juc2 - Just Use Curses (Mark 2)',
    license='MIT',
    url='https://github.com/vesche/juc2',
    author=juc2.__author__,
    author_email=juc2.__email__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Artistic Software",
        "Topic :: Terminals"
    ]
)
