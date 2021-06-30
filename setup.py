#! /usr/bin/env python

from setuptools import setup

setup(name="SAKHAR Protect",
      version="1.0",
      description="Protection contre les ransomwares",
      install_requires=["colorama",
                        "requests",
                        "Werkzeug",
                        "watchdog",
                        "pypiwin32",
                        "pywin32",
                        "cryptography"]
      )
