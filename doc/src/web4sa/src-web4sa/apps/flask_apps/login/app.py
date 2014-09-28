import os
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.secret_key = os.urandom(24)

# Email settings
import base64
app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME = 'cbcwebsolvermail@gmail.com',
        MAIL_PASSWORD = base64.decodestring('RGlmZmljdWx0UFch'),
        MAIL_DEFAULT_SENDER = 'Flask Compute Email <cbcwebsolvermail@gmail.com>'
        )
