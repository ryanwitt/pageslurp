#!/bin/sh -e
# bootstraps the local virtual environment
~/local/bin/virtualenv --no-site-packages --distribute --python=python2.5 python_environment
. python_environment/bin/activate
pip install -r REQUIREMENTS
