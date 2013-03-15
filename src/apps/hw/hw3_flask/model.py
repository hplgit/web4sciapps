from wtforms import Form, FloatField, validators

class InputForm(Form):
    r = FloatField(validators=[validators.required()])

