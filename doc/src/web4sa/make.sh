#!/bin/sh
# Compile document in HTML versions, Flask+Django, Flask only,
# Django only, Sphinx version, and LaTeX/PDF version.

sh clean.sh

name=web4sa
doconce format html $name -DTOPIC=Flask+Django --html_style=bloodish
if [ $? -ne 0 ]; then exit; fi
cp $name.html ${name}_plain_all.html
cp $name.html ${name}_plain.html
doconce split_html ${name}_plain
if [ $? -ne 0 ]; then exit; fi

doconce format html ${name}_flask -DTOPIC=Flask --html_style=vagrant --html_template=html_templates/template_flask.html
if [ $? -ne 0 ]; then exit; fi
doconce split_html ${name}_flask
if [ $? -ne 0 ]; then exit; fi

doconce format html ${name}_django -DTOPIC=Django --html_style=vagrant --html_template=html_templates/template_django.html
if [ $? -ne 0 ]; then exit; fi
cp ${name}_django.html tmp.html
doconce split_html ${name}_django
if [ $? -ne 0 ]; then exit; fi

doconce format sphinx $name -DTOPIC=Flask+Django
doconce split_rst $name
if [ $? -ne 0 ]; then exit; fi
doconce sphinx_dir author='H. P. Langtangen and A. E. Johansen' $name theme=basicstrap
if [ $? -ne 0 ]; then exit; fi
python automake_sphinx.py
if [ $? -ne 0 ]; then exit; fi
cd sphinx-rootdir
sh make_themes.sh cbc bootstrap basicstrap pyramid redcloud
cd ..
mv sphinx-rootdir/sphinx-* .

doconce format pdflatex $name -DTOPIC=Flask+Django
if [ $? -ne 0 ]; then exit; fi
doconce ptex2tex $name envir=minted
pdflatex -shell-escape $name
makeindex $name
pdflatex -shell-escape $name
pdflatex -shell-escape $name

doconce format html index --html-style=bloodish

# Publish
#dest=../../pub
#cp -r *.html .*.html fig-$name sphinx-* $dest
#rm -rf $dest/sphinx-rootdir
