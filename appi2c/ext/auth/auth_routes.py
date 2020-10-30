from flask import (Blueprint,
                   redirect,
                   url_for,
                   flash,
                   render_template,
                   request)
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
        return redirect(url_for('login.index'))
    form = UserForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        create_user(username=form.username.data, email=form.email.data, password=hash_password, admin=form.admin.data)
        flash('Your account has benn created! Log in now', 'success')
        return redirect(url_for('login.login'))
    return render_template('login/signup.html', title='Signup', form=form)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = login_check_user(username=form.username.data)
        if user is None or not login_check_password_hash(user.password, form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('site.index')
        return redirect(next_page)        
    return render_template('login/login.html', title='Login', form=form)


@bp.route("/logout")
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
        update_profile(user, current_user.username, current_user.email ,current_user.password)
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('site.index'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.password.data = current_user.password
        form.confirm_password.data = current_user.password
    return render_template('login/edit_profile.html', title='Edit Profile', form=form)
