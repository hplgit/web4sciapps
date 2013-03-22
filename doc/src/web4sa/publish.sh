#!/bin/sh
name=web4sa
cp -r *.html .*.html html_templates sphinx-* $name.pdf fig-$name ../../pub/
rm -rf ../../pub/sphinx-rootdir  # remove this if it was copied
