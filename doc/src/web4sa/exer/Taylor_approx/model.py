from wtforms import Form, TextField, SelectField, IntegerField, validators
from math import pi

class InputForm(Form):
    Variable = TextField(
        label='Name of independent variable',
        default='x',
        validators=[validators.InputRequired()])
    Formula = TextField(
        label='Expression in independent variable',
        default='sin(x)',
        validators=[validators.InputRequired()])
    xmin = TextField(
        label='Minimum x value in the plot', default='0',
        validators=[validators.InputRequired()])
    xmax = TextField(
        label='Maximum x value in the plot', default='2*pi',
        validators=[validators.InputRequired()])
    ymin = TextField(
        label='Minimum y value in the plot', default='-2',
        validators=[validators.InputRequired()])
    ymax = TextField(
        label='Maximum y value in the plot', default='2',
        validators=[validators.InputRequired()])
    x0 = TextField(
        label='Point for series expansion', default='0',
        validators=[validators.InputRequired()])
    N = IntegerField(
        label='Polynomial degree of series approximation', default=7,
        validators=[validators.InputRequired()])
    legend_loc = TextField(
        label='Location of legend in the plot', default='lower left',
        validators=[validators.InputRequired()])
    Erase = SelectField(
        label='Erase all curves?',
        # choices is (value, label) pairs: label gets printed
        # value is form.Erase.data
        choices=[('yes', 'Yes'), ('no', 'No')], default=2)
