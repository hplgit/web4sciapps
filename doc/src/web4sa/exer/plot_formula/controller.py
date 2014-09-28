from model import InputForm
from flask import Flask, render_template, request
from compute import plot_formula as compute

app = Flask(__name__)

@app.route('/formula', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.Formula.data, form.Domain.data,
                         form.Erase.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
