from flask import Flask, render_template, request
from model import InputForm
from compute import compute

app = Flask(__name__)

@app.route('/vib2', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        for field in form:
            # Make local variable (name field.name)
            exec('%s = %s' % (field.name, field.data))
        result = compute(A, b, w, T)
    else:
        result = None

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
