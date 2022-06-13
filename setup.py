#!/usr/bin/env python3
#

import os
from setuptools import setup


def read(fname):
    """Read a file and return the content"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="zyzzbot",
    version="0.0.1",
    author="Seburath",
    author_email="t.me/seburath",
    description=("Zyzz bot"),
    license="MIT",
    keywords="zyzzbot bodyfat calculator ffmi calculator",
    url="http://github.com/seburath/body-fat-calculator-bot",
    packages=["zyzzbot"],  # , "tests"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Management",
        "License :: OSI Approved :: MIT License",
    ],
)
