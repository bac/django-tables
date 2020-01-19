#!/usr/bin/env python
import os
from setuptools import setup, find_packages


# Figure out the version; this could be done by importing the
# module, though that requires Django to be already installed,
# which may not be the case when processing a pip requirements
# file, for example.
import re

here = os.path.dirname(os.path.abspath(__file__))
version_re = re.compile(r"__version__ = (\(.*?\))")
fp = open(os.path.join(here, "django_tables", "__init__.py"))
version = None
for line in fp:
    match = version_re.search(line)
    if match:
        version = eval(match.group(1))
        break
else:
    raise Exception("Cannot find version in __init__.py")
fp.close()

setup(
    name="django-tables",
    version=".".join(map(str, version)),
    description="Render QuerySets as tabular data in Django.",
    author="Michael Elsdoerfer",
    author_email="michael@elsdoerfer.info",
    license="BSD",
    url="http://launchpad.net/django-tables",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(),
)
