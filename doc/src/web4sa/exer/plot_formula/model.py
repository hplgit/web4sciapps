from wtforms import Form, TextField, SelectField, validators
from math import pi

class InputForm(Form):
    Formula = TextField(
        label='Expression in x',
        default='sin(x)',
        validators=[validators.InputRequired()])
    Domain = TextField(
        label='Domain: [xmin, xmax]', default='[0, 2*pi]',
        validators=[validators.InputRequired()])
    Erase = SelectField(
        label='Erase all curves?',
        # choices is (value, label) pairs: label gets printed
        # value is form.Erase.data
        choices=[('yes', 'Yes'), ('no', 'No')], default=2)
