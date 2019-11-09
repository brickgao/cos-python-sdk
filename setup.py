#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from contentos_sdk import __version__

tests_requirements = [
    "mock == 3.0.5",
    "pytest == 5.2.2"
]

setup(
    name="contentos_sdk",
    version=__version__,
    url="https://github.com/brickgao/cos-python-sdk",
    license="MIT",
    description="Python SDK for Contentos",
    long_description=open("README.md").read(),
    author="Xiongzhi Gao",
    author_email="brickgao@gmail.com",
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    install_requires=[
        "base58 == 1.0.3",
        "grpcio == 1.22.0",
        "grpcio-tools == 1.22.0",
        "pycrypto == 2.6.1",
        "secp256k1 == 0.13.2"
    ] + tests_requirements,
    tests_require=tests_requirements,
    test_suite="nose.collector",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)