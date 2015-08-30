#!/bin/sh
# Compile document in HTML versions, Flask+Django, Flask only,
# Django only, Sphinx version, and LaTeX/PDF version.
set -x
sh clean.sh

function system {
  "$@"
  if [ $? -ne 0 ]; then
    echo "make.sh: unsuccessful command $@"
    echo "abort!"
    exit 1
  fi
}

name=web4sa

system doconce format html $name -DTOPIC=Flask+Django --html_style=bloodish
cp $name.html ${name}_plain_all.html
cp $name.html ${name}_plain.html
system doconce split_html ${name}_plain --nav_button=text

system doconce format html $name -DTOPIC=Flask+Django --html_style=solarized3
cp $name.html ${name}_solarized.html
system doconce split_html ${name}_solarized --nav_button=text

system doconce format html ${name} -DTOPIC=Flask --html_style=bootstrap --html_template=html_templates/template_flask.html --html_output=${name}_flask
system doconce split_html ${name}_flask

system doconce format html ${name} -DTOPIC=Django --html_style=bootstrap --html_template=html_templates/template_django.html --html_output=${name}_django
system doconce split_html ${name}_django

system doconce format sphinx $name -DTOPIC=Flask+Django
system doconce split_rst $name
system doconce sphinx_dir copyright='H. P. Langtangen and A. E. Johansen' $name theme=basicstrap
system python automake_sphinx.py
cd sphinx-rootdir
sh make_themes.sh cbc basicstrap redcloud
cd ..
mv sphinx-rootdir/sphinx-* .


system doconce format pdflatex $name -DTOPIC=Flask+Django
system doconce ptex2tex $name envir=minted
system pdflatex -shell-escape $name
makeindex $name
pdflatex -shell-escape $name
pdflatex -shell-escape $name

doconce format html index --html_style=bootstrap --html_boostrap_jumbotron=off --html_bootstrap_navbar=off

# Publish
dest=../../pub
rm -rf $dest/sphinx-rootdir $dest/sphinx-*
rm -rf sphinx-rootdir
cp -r ${name}*.html .*${name}*.html $name.pdf sphinx-* $dest
cp -r fig-$name/* $dest/fig-$name/
cp index.html $dest
