from model import InputForm
from flask import Flask, render_template, request
from compute import visualize_series as compute

app = Flask(__name__)

@app.route('/Taylor', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(formula=form.Formula.data,
                         independent_variable=form.Variable.data,
                         N=form.N.data,
                         xmin=form.xmin.data,
                         xmax=form.xmax.data,
                         ymin=form.ymin.data,
                         ymax=form.ymax.data,
                         legend_loc=form.legend_loc.data,
                         x0=form.x0.data,
                         erase=form.Erase.data)
    else:
        result = None
    print request.method, [field.errors for field in form]

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
