#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-picked",
    version="0.1.0",
    author="Ana Paula Gomes",
    author_email="apgomes88@gmail.com",
    maintainer="Ana Paula Gomes",
    maintainer_email="apgomes88@gmail.com",
    license="MIT",
    url="https://github.com/anapaulagomes/pytest-picked",
    description="Run the tests related to the changed files",
    long_description=read("README.rst"),
    py_modules=["pytest_picked"],
    python_requires=">=3.5",
    install_requires=["pytest>=3.5.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["picked = pytest_picked"]},
)
