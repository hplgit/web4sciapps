"""
Example on generic model.py file which inspects the arguments
of the compute function and automatically generates a relevant
InputForm class.
"""

import wtforms
from math import pi
from compute import compute_gamma as compute
import numpy as np
import inspect
arg_names = inspect.getargspec(compute).args
defaults  = inspect.getargspec(compute).defaults

class InputForm(wtforms.Form):
    pass

# Augment defaults with None elements for the positional
# arguments
defaults = [None]*(len(arg_names)-len(defaults)) + list(defaults)
# Map type of default to right form field
type2form = {type(1.0): wtforms.FloatField,
             type(1):   wtforms.IntegerField,
             type(''):  wtforms.TextField,
             type([]):  wtforms.TextField,
             type(()):  wtforms.TextField,
             type(np.array([1,2.])):  wtforms.TextField,
             }

def get_type_as_str(obj):
    return str(type(obj)).split("'")[1]

for name, value in zip(arg_names, defaults):
    if value is None:
        setattr(InputForm, name, wtforms.FloatField(
            validators=[wtforms.validators.InputRequired()]))
    else:
        if type(value) in type2form:
            setattr(InputForm, name, type2form[type(value)](
                default=value,
                label='(%s)' % get_type_as_str(value),
                validators=[wtforms.validators.InputRequired()]))
        else:
            raise TypeError('argument %s %s not supported' %
                            name, type(value))

if __name__ == '__main__':
    for item in dir(InputForm):
        if item in arg_names:
            print item, getattr(InputForm, item)
