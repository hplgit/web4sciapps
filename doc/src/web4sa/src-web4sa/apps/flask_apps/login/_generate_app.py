"""
This file is not part of the web application in this directory.

This file just applies the Parampool package to automatically generate
a Flask app with login functionality. It was used as starting
point for the files in this directory, but the files have been
edited (and simplified) afterwards.
"""
from parampool.generator.flask import generate
from compute import compute_gamma

generate(compute_gamma, default_field='FloatField', enable_login=True)
