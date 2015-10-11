from wtforms import Form, FloatField

class AddForm(Form):
    a = FloatField(label='', default=1.0)
    b = FloatField(label='', default=1.0)

class MulForm(Form):
    p = FloatField(label='', default=2)
    q = FloatField(label='', default=2)
