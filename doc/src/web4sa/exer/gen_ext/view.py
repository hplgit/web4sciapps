from model import InputForm
from flask import Flask, render_template, request
from compute import compute_gamma as compute
import sys, os, inspect

app = Flask(__name__)

@app.route('/vib3_ext', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        arg_names = inspect.getargspec(compute).args
        kwargs = {name: getattr(form, name).data
                  for name in arg_names if hasattr(form, name)}
        # Run eval on the text
        # Note that form.name.label is <label for="A">(list)</label>
        for name in kwargs:
            if hasattr(form, name) and \
                   hasattr(getattr(form, name), 'label'):
                label = str(getattr(form, name).label)
                for tp in ('(list)', '(tuple)', '(nd.array)'):
                    if tp in label:
                        kwargs[name] = eval(kwargs[name])

        result = compute(**kwargs)
    else:
        result = None
    if result:
        # result must be transformed to HTML and inserted as a
        # string in the generic view.html file
        result = render_template('view_results.html', result=result)
    return render_template('view.html', form=form, result=result)
