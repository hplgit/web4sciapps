from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)

@app.route('/hw3', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
    else:
        s = None

    return render_template("view.html", form=form, s=s)


if __name__ == '__main__':
    app.run(debug=True)
