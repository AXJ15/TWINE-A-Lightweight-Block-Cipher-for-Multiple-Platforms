import sys
import os
from setuptools import setup

_locals = {}
exec(open("src/_version.py").read(), None, _locals)
version = _locals["__version__"]
long_description = open("README.md").read()

setup(
    name="twine",
    version=version,
    packages=["twine"],
    package_dir={"twine": "src"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amoallim15/TWINE",
    author="Ali Moallim",
    author_email="amoallim15@gmail.com",
    keywords="twine cipher encryption decryption",
    entry_points={"console_scripts": ["twine = src.__main__:main"]},
    licence="MIT",
    platforms=["all"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Scientists",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)