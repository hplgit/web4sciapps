#!/bin/sh
name=web4sa
doconce clean
rm -rf ${name}_*.html sphinx-* automake_sphinx.py
rm -rf src-${name}/apps/vib/vib1_flask/static/*.png
rm -rf src-${name}/apps/vib/vib3_flask/static
rm -rf src-${name}/apps/vib/vib1_django/static
rm -rf src-${name}/apps/vib/vib2_django/static
