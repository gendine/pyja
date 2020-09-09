#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import pyja

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = []
setup(
    author=pyja.__author__,
    author_email=pyja.__email__,
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description=pyja.__description__,
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    entry_points={"console_scripts": ["pyja = pyja.__main__:main"]},
    include_package_data=True,
    keywords="pyja",
    name="pyja",
    packages=find_packages(include=["pyja", "pyja.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/gendine/pyja",
    license=pyja.__licence__,
    version=pyja.__version__,
    zip_safe=False,
)
