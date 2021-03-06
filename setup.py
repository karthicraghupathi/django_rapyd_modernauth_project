#!/usr/bin/env python

import os

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


with open("README.rst") as f:
    readme = f.read()


with open("LICENSE") as f:
    license = f.read()


setup(
    name="django-rapyd-modernauth",
    version="0.0.1",
    description="Provides a custom User model where the username is the email address.",
    long_description=readme,
    author="Karthic Raghupathi",
    author_email="karthicr@gmail.com",
    url="https://github.com/karthicraghupathi/django_rapyd_modernauth_project",
    license=license,
    package_dir={"": "src"},
    packages=["modernauth", "modernauth.migrations"],
    install_requires=["django>=3,<3.3"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
