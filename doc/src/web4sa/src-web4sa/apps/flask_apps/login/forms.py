import wtforms as wtf

# Application data
class GammaForm(wtf.Form):
    a = wtf.FloatField(default=0.5,
        validators=[wtf.validators.InputRequired()])
    h = wtf.FloatField(default=2.0,
        validators=[wtf.validators.InputRequired()])
    A = wtf.FloatField(default=1.41421356237,
        validators=[wtf.validators.InputRequired()])
    resolution = wtf.IntegerField(default=500,
        validators=[wtf.validators.InputRequired()])

from db_models import db, User
import flask.ext.wtf.html5 as html5

# Standard forms for login
class register_form(wtf.Form):
    username = wtf.TextField(
        'Username', [wtf.validators.Required()])
    password = wtf.PasswordField(
        'Password', [wtf.validators.Required(),
                     wtf.validators.EqualTo(
                         'confirm',
                         message='Passwords must match')])
    confirm  = wtf.PasswordField(
        'Confirm Password', [wtf.validators.Required()])
    email    = html5.EmailField('Email')
    notify   = wtf.BooleanField('Email notifications')

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
        'Username', [wtf.validators.Required()])
    password = wtf.PasswordField(
        'Password', [wtf.validators.Required()])

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
