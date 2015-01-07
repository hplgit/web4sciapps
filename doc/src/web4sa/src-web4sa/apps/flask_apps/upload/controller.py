from compute import compute_mean_std as compute_function

from flask import Flask, render_template, request
from model import Average
from werkzeug import secure_filename
import os

# Application object
app = Flask(__name__)

# Relative path of directory for uploaded files
UPLOAD_DIR = 'uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
app.secret_key = 'MySecretKey'

if not os.path.isdir(UPLOAD_DIR):
    os.mkdir(UPLOAD_DIR)

# Allowed file types for file upload
ALLOWED_EXTENSIONS = set(['txt', 'dat', 'npy'])

def allowed_file(filename):
    """Does filename have the right extension?"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Path to the web application
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Average(request.form)
    filename = None  # default
    if request.method == 'POST':

        # Save uploaded file on server if it exists and is valid
        if request.files:
            file = request.files[form.filename.name]
            if file and allowed_file(file.filename):
                # Make a valid version of filename for any file ystem
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                       filename))

        result = compute_function(filename)
    else:
        result = None

    return render_template("view.html", form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
