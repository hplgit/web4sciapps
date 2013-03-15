from wtforms import Form, FloatField, validators
from math import pi
import functools

def check_interval(form, field, min_value=None, max_value=None):
    """Validate that a form field is inside an interval."""
    failure = False
    if min_value is not None:
        if field.data < min_value:
            failure = True
    if max_value is not None:
        if field.data > max_value:
            failure = True
    print min_value, max_value
    min_value = '-infty' if min_value is None else str(min_value)
    max_value =  'infty' if max_value is None else str(max_value)
    print min_value, max_value
    if failure:
        raise validators.ValidationError(
            '%s=%s not in [%s, %s]' % (field.name, field.data,
                                       min_value, max_value))

def interval(min_value=None, max_value=None):
    """Short-hand function."""
    return functools.partial(
        check_interval, min_value=min_value, max_value=max_value)

def check_T(form, field):
    # Failure if more than 30 periods
    period = 2*pi/form.w.data
    if field.data > 30*period:
        num_periods = int(round(field.data/period))
        raise validators.ValidationError(
            'Cannot plot as much as %d periods! T<%.2f' %
            (num_periods, 30*period))

class InputForm(Form):
    A = FloatField(
        label='amplitude (m)', default=1.0,
        validators=[interval(0,None), validators.InputRequired()])
    b = FloatField(
        label='damping factor (kg/s)', default=0,
        validators=[interval(0,None), validators.InputRequired()])
    w = FloatField(
        label='frequency (1/s)', default=2*pi,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='time interval', default=6*pi,
        validators=[check_T, validators.InputRequired()])
