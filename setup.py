#!/usr/bin/env python
# Copyright (C) 2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - https://cuckoosandbox.org/.
# See the file 'docs/LICENSE' for copying permission.

import setuptools

setuptools.setup(
    name="quailbox",
    version="0.1.1",
    author="Daan Spitz",
    author_email="daan@cuckoo.sh",
    packages=[
        "quailbox",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Pytest",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
    ],
    url="https://cuckoosandbox.org/",
    license="GPLv3",
    description="IoT honeypotting and fuzzing framework for Cuckoo/QEMU",
    long_description=open("README.md", "rb").read(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "quailbox = quailbox.main:main",
        ],
    },
    install_requires=[
        "click==6.7",
        "glob2==0.6",
        "mock==2.0.0",
        "PyYAML==3.12",
    ],
    setup_requires=[
        "pytest-runner",
    ],
    tests_require=[
        "coveralls",
        "pytest",
        "pytest-cov",
        "mock==2.0.0",
    ],
)
