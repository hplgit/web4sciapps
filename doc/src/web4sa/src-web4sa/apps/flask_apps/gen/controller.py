from model import InputForm
from flask import Flask, render_template, request
from compute import compute_gamma as compute
import sys, os, inspect

app = Flask(__name__)

@app.route('/vib4', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        arg_names = inspect.getargspec(compute).args
        kwargs = {name: getattr(form, name).data
                  for name in arg_names if hasattr(form, name)}
        result = compute(**kwargs)
    else:
        result = None
    if result:
        # result must be transformed to HTML and inserted as a
        # string in the generic view.html file
        result = render_template('view_results.html', result=result)
    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
