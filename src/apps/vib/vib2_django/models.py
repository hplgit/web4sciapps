from django.db import models
from django.forms import ModelForm
from math import pi
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
import functools

def check_interval(value, min_value=None, max_value=None):
    """Validate that a value is inside an interval."""
    failure = False
    if min_value is not None:
        if value < min_value:
            failure = True
    if max_value is not None:
        if value > max_value:
            failure = True
    min_value = '-infty' if min_value is None else str(min_value)
    max_value =  'infty' if max_value is None else str(max_value)
    if failure:
        raise ValidationError(
            'value=%s not in [%s, %s]' %
            (value, min_value, max_value))

def interval(min_value=None, max_value=None):
    """Django-compatible interface to check_interval."""
    return functools.partial(
        check_interval, min_value=min_value, max_value=max_value)

class Input(models.Model):
    A = models.FloatField(
        verbose_name=' amplitude (m)', default=1.0,
        validators=[MinValueValidator(0)])
    b = models.FloatField(
        verbose_name=' damping coefficient (kg/s)', default=0.0,
        validators=[interval(0,None)])
    w = models.FloatField(
        verbose_name=' frequency (1/s)', default=2*pi)
    T = models.FloatField(
        verbose_name=' time interval (s)', default=18)

class InputForm(ModelForm):
    class Meta:
        model = Input

    def clean_T(self):
        T = self.cleaned_data['T']
        w = self.cleaned_data['w']
        period = 2*pi/w
        if T > 30*period:
            num_periods = int(round(T/period))
            raise ValidationError(
                'Cannot plot as much as %d periods! T<%.2f' %
                (num_periods, 30*period))
        return T
