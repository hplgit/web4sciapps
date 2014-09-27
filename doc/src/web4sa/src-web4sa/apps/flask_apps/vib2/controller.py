from flask import Flask, render_template, request
from model import InputForm
import sys
# SVG or PNG plot?
svg = False
try:
    if sys.argv[1] == 'svg':
        svg = True
except IndexError:
    pass
if svg:
    from compute import compute_png_svg as compute
    template = 'view_svg.html'
else:
    from compute import compute
    template = 'view.html'

app = Flask(__name__)

@app.route('/vib2', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        for field in form:
            # Make local variable (name field.name)
            exec('%s = %s' % (field.name, field.data))
        result = compute(A, b, w, T)
        import codecs
        f = codecs.open('tmp.svg', 'w', 'utf-8')
        f.write(result[1])
        f.close()
    else:
        result = None

    return render_template(template, form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
