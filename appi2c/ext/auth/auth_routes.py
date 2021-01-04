from flask import (Blueprint,
                   redirect,
                   url_for,
                   flash,
                   render_template,
                   request,
                   jsonify)
from werkzeug.urls import url_parse
from flask_login import (current_user,
                         login_required,
                         logout_user,
                         login_user)
from appi2c.ext.auth.auth_forms import (UserForm,
                                        EditProfile)
from appi2c.ext.encrypt import bcrypt
from appi2c.ext.auth.auth_controller import create_user
from appi2c.ext.auth.auth_forms import LoginForm
from appi2c.ext.auth.auth_controller import (login_check_user,
                                             login_check_password_hash,
                                             update_profile)


bp = Blueprint("login", __name__, template_folder="appi2c/templates/login")


@bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    form = UserForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        create_user(username=form.username.data, email=form.email.data, password=hash_password, admin=form.admin.data)
        flash('Your account has benn created! Congratulations', 'success')
        return redirect(url_for('site.index'))
    return render_template('login/signup.html', title='Signup', form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    else:
        _json = request.json
        _username = _json['username']
        _password = _json['password']

    if _username and _password:
        user = login_check_user(username=_username)
        if user is None or not login_check_password_hash(user.password, _password):
            resp = jsonify({'message': 'Ajax Bad Request - Error auth_routes.py @bp.route(/login)'})
            resp.status_code = 400
            return resp
        else:
            login_user(user)
            return jsonify({'message': 'user successfully logged'})
    else:
        resp = jsonify({'message': 'Invalid credendtials'})
        resp.status_code = 400
        return resp


@bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.index'))


@bp.route('/editProfile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfile()
    user = current_user
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        current_user.password = hash_password
        current_user.confirm_password = form.confirm_password.data
        update_profile(user, current_user.username, current_user.email, current_user.password)
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('site.index'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.password.data = current_user.password
        form.confirm_password.data = current_user.password
    return render_template('login/edit_profile.html', title='Edit Profile', form=form)
