from model import AddForm, MulForm
from flask import Flask, render_template, request
from compute import add, mul

app = Flask(__name__)

@app.route('/addmul', methods=['GET', 'POST'])
def index():
    form = {}
    result = {}

    # Try to make as common code as possible for the two apps
    name = 'add'
    f = form[name] = AddForm(request.form)
    if request.method == 'POST' and f.validate() and \
           request.form['btn'] == 'Add':
        result[name] = add(f.a.data, f.b.data)
    else:
        result[name] = None

    name = 'mul'
    f = form[name] = MulForm(request.form)
    if request.method == 'POST' and f.validate() and \
           request.form['btn'] == 'Multiply':
        result[name] = mul(f.p.data, f.q.data)
    else:
        result[name] = None

    return render_template('view.html',
                           form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
