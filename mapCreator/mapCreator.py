#!/usr/bin/env python3

import sys
MIN_PYTHON = (3,6)
if sys.version_info < MIN_PYTHON:
    raise Exception("Python version %s or higher is required." %(MIN_PYTHON))

import cli
if __name__ == "__main__":
    cli.main()
