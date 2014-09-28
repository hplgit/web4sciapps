import wtforms as wtf
from math import pi

class ComputeForm(wtf.Form):
    A = wtf.FloatField(label='\( A \)', default=1.0,
        validators=[wtf.validators.InputRequired()])
    b = wtf.FloatField(label='\( b \)', default=0.0,
        validators=[wtf.validators.InputRequired()])
    w = wtf.FloatField(label='\( w \)', default=pi,
        validators=[wtf.validators.InputRequired()])
    T = wtf.FloatField(label='\( T \)', default=18,
        validators=[wtf.validators.InputRequired()])
    resolution = wtf.IntegerField(label='resolution', default=500,
        validators=[wtf.validators.InputRequired()])

from db_models import db, User
import flask.ext.wtf.html5 as html5

# Standard Forms
class register_form(wtf.Form):
    username = wtf.TextField(
        label='Username', validators=[wtf.validators.Required()])
    password = wtf.PasswordField(
        label='Password', validators=[
            wtf.validators.Required(),
            wtf.validators.EqualTo(
                'confirm', message='Passwords must match')])
    confirm  = wtf.PasswordField(
        label='Confirm Password',
        validators=[wtf.validators.Required()])
    email    = html5.EmailField(label='Email')
    notify   = wtf.BooleanField(label='Email notifications')

    def validate(self):
        if not wtf.Form.validate(self):
            return False

        if self.notify.data and not self.email.data:
            self.notify.errors.append(
        'Cannot send notifications without a valid email address')
            return False

        if db.session.query(User).filter_by(
            username=self.username.data).count() > 0:
            self.username.errors.append('User already exists')
            return False

        return True

class login_form(wtf.Form):
    username = wtf.TextField(
        label='Username', validators=[wtf.validators.Required()])
    password = wtf.PasswordField(
        label='Password', validators=[wtf.validators.Required()])

    def validate(self):
        if not wtf.Form.validate(self):
            return False

        user = self.get_user()

        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        return True

    def get_user(self):
        return db.session.query(User).filter_by(
            username=self.username.data).first()
