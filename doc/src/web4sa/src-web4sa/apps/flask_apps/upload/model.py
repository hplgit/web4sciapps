import wtforms as wtf

class Average(wtf.Form):
    filename   = wtf.FileField(validators=
                               [wtf.validators.InputRequired()])
