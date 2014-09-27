from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    pwhash = db.Column(db.String())
    email = db.Column(db.String(120), nullable=True)
    notify = db.Column(db.Boolean())

    def __repr__(self):
        return '<User %r>' % (self.username)

    def check_password(self, pw):
        return check_password_hash(self.pwhash, pw)

    def set_password(self, pw):
        self.pwhash = generate_password_hash(pw)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

class Gamma(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    a          = db.Column(db.Float)
    h          = db.Column(db.Float)
    A          = db.Column(db.Float)
    resolution = db.Column(db.Integer)

    result   = db.Column(db.String())
    comments = db.Column(db.String(), nullable=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    user     = db.relationship('User',
                backref=db.backref('Gamma', lazy='dynamic'))