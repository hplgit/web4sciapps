import os
from compute import compute as compute_function

from flask import Flask, render_template, request, redirect, url_for
from forms import ComputeForm
from db_models import db, User, Compute
from flask.ext.login import LoginManager, current_user, \
     login_user, logout_user, login_required
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

# Path to the web application
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user = current_user
    form = ComputeForm(request.form)
    if request.method == "POST":
        if form.validate():

            result = compute_function(form.A.data, form.b.data,
                                      form.w.data, form.T.data)
            if user.is_authenticated():
                object = Compute()
                form.populate_obj(object)
                object.result = result
                object.user = user
                db.session.add(object)
                db.session.commit()

                # Send email notification
                if user.notify and user.email:
                    send_email(user)
    else:
        if user.is_authenticated():
            if user.Compute.count() > 0:
                instance = user.Compute.order_by('-id').first()
                result = instance.result
                form = populate_form_from_instance(instance)

    return render_template("view.html", form=form,
                           result=result, user=user)


def populate_form_from_instance(instance):
    """Repopulate form with previous values"""
    form = ComputeForm()
    for field in form:
        field.data = getattr(instance, field.name)
    return form

def send_email(user):
    from flask.ext.mail import Mail, Message
    mail = Mail(app)
    msg = Message("Compute Computations Complete",
                  recipients=[user.email])
    msg.body = """
A simulation has been completed by the Flask Compute app.
Please log in at

http://localhost:5000/login

to see the results.

---
If you don't want email notifications when a result is found,
please register a new user and leave the 'notify' field
unchecked.
"""
    mail.send(msg)

@app.route('/reg', methods=['GET', 'POST'])
def create_login():
    from forms import register_form
    form = register_form(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        form.populate_obj(user)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('index'))
    return render_template("reg.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    from forms import login_form
    form = login_form(request.form)
    if request.method == 'POST' and form.validate():
        user = form.get_user()
        login_user(user)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/old')
@login_required
def old():
    data = []
    user = current_user
    if user.is_authenticated():
        instances = user.Compute.order_by('-id').all()
        for instance in instances:
            form = populate_form_from_instance(instance)

            result = instance.result
            if instance.comments:
                comments = "<h3>Comments</h3>" + instance.comments
            else:
                comments = ''
            data.append(
                {'form':form, 'result':result,
                 'id':instance.id, 'comments': comments})

    return render_template("old.html", data=data)

@app.route('/add_comment', methods=['GET', 'POST'])
@login_required
def add_comment():
    user = current_user
    if request.method == 'POST' and user.is_authenticated():
        instance = user.Compute.order_by('-id').first()
        instance.comments = request.form.get("comments", None)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    id = int(id)
    user = current_user
    if user.is_authenticated():
        if id == -1:
            instances = user.Compute.delete()
        else:
            try:
                instance = user.Compute.filter_by(id=id).first()
                db.session.delete(instance)
            except:
                pass

        db.session.commit()
    return redirect(url_for('old'))


if __name__ == '__main__':
    if not os.path.isfile(os.path.join(
        os.path.dirname(__file__), 'sqlite.db')):
        db.create_all()
    app.run(debug=True)
