from model import InputForm
from flask import Flask, render_template, request
from compute import compute_gamma as compute
import sys, os, inspect

app = Flask(__name__)

@app.route('/vib3', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        arg_names = inspect.getargspec(compute).args
        kwargs = {name: getattr(form, name).data
                  for name in arg_names if hasattr(form, name)}
        result = compute(**kwargs)
    else:
        result = None
    # Concatenate view_forms.html and view_results.html
    forms_html   = os.path.join('templates', 'view_forms.html')
    results_html = os.path.join('templates', 'view_results.html')
    view_html    = os.path.join('templates', 'view.html')
    f_forms = open(forms_html, 'r')
    f_res   = open(results_html, 'r')
    f_view  = open(view_html, 'w')
    f_view.write(f_forms.read() + f_res.read())
    f_forms.close();  f_res.close();  f_view.close()
    return render_template(os.path.basename(view_html),
                           form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
