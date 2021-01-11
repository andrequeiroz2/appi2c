from appi2c.ext.database import db
from flask import flash, render_template, redirect, url_for, request, Blueprint, jsonify
from flask_login import login_required, current_user
from appi2c.ext.notifier.notifier_forms import NotifierForm, EditNotifierForm
from appi2c.ext.notifier.notifier_controller import (create_notifier,
                                                     list_notifier_id,
                                                     list_all_notifier,
                                                     update_notifier,
                                                     delete_notifier_id,
                                                     list_notifier_serializable_user)


bp = Blueprint('notifiers', __name__, template_folder='appi2c/templates/notifier')


@bp.route("/register/notifier", methods=['GET', 'POST'])
@login_required
def register_notifier():

    form = NotifierForm()

    if form.validate_on_submit():

        create_notifier(name=form.name.data,
                        token=form.token.data,
                        chat_id=form.chat_id.data,
                        user_id=current_user.id)
        flash('Notifier has benn created!', 'success')
        return redirect(url_for('site.index'))

    return render_template('notifier/notifier_create.html', title='Register Notifier', form=form)


@bp.route("/options/notifier", methods=['GET', 'POST'])
@login_required
def notifier_opts():
    return render_template("notifier/notifier_opts.html",
                           title='Notifier Options')


@bp.route("/list/notifier", methods=['GET', 'POST'])
@login_required
def list_notifier():
    notifiers = list_all_notifier(current_user)
    if not notifiers:
        flash('There are no records. Register a Notifier', 'error')
        return redirect(url_for('notifiers.notifier_opts'))
    return render_template("notifier/notifier_list.html",
                           title='Notifier List',
                           notifiers=notifiers)


@bp.route('/edit/notifier/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_notifier(id):
    form = EditNotifierForm()

    current_notifier = list_notifier_id(id)

    if form.validate_on_submit():
        current_notifier.name = form.name.data
        current_notifier.token = form.token.data
        current_notifier.chat_id = form.chat_id.data

        update_notifier(current_notifier.id,
                        current_notifier.name,
                        current_notifier.token,
                        current_notifier.chat_id)

        flash('Your changes have been saved.', 'success')
        return redirect(url_for('notifiers.admin_notifier'))

    elif request.method == 'GET':
        form.name.data = current_notifier.name
        form.token.data = current_notifier.token
        form.chat_id.data = current_notifier.chat_id

    return render_template('notifier/notifier_edit.html', title='Edit Notifier', form=form)


@bp.route("/admin/notifiers", methods=['GET', 'POST'])
@login_required
def notifier_admin():
    notifiers = list_all_notifier(current_user)
    if not notifiers:
        flash('There are no records. Register a Notifier', 'error')
        return redirect(url_for('notifiers.notifier_opts'))
    return render_template('notifier/notifier_admin.html',
                           title='Notifier Admin',
                           notifiers=notifiers)


@bp.route('/delete/notifier/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_notifier(id):
    delete_notifier_id(id)
    return redirect(url_for('notifiers.notifier_opts'))


@bp.route('/list/notifier/ajax', methods=['GET', 'POST'])
@login_required
def get_notifier():
    notifiers = list_notifier_serializable_user(current_user)
    return jsonify(notifiers)
