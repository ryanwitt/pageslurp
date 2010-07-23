#!/bin/sh -e
# bootstraps the local virtual environment
virtualenv --no-site-packages --distribute python_environment
. python_environment/bin/activate
pip install -r REQUIREMENTS
