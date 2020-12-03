from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required
from flask import Blueprint
from appi2c.ext.icon.icon_forms import IconForm, EditIconForm
from appi2c.ext.icon.icon_controller import (list_all_icon,
                                             list_icon_id,
                                             create_icon,
                                             update_icon)


bp = Blueprint('icons', __name__, template_folder="appi2c/templates/icon")


@bp.route("/register/icon", methods=['GET', 'POST'])
@login_required
def register_icon():
    form = IconForm()
    if form.validate_on_submit():
        create_icon(html_class=form.html_class.data)
        flash('Icon has benn created!', 'success')
        return redirect(url_for('icons.admin_icon'))
    return render_template('icon/icon_create.html', title='Register Icon', form=form)


@bp.route("/admin/icon", methods=['GET', 'POST'])
@login_required
def admin_icon():
    icons = list_all_icon()
    if not icons:
        flash('There are no records. Register a icon', 'error')
        return redirect(url_for('icons.register_icon'))
    return render_template('icon/icon_admin.html', title='Icon Admin', icons=icons)


@bp.route('/edit/icon/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_icon(id):
    form = EditIconForm()
    current_icon = list_icon_id(id)
    if form.validate_on_submit():
        current_icon.html_class = form.html_class.data
        update_icon(id, current_icon.html_class)
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('icons.admin_icon'))
    elif request.method == 'GET':
        form.html_class.data = current_icon.html_class
    return render_template('icon/edit_icon.html', title='Edit Icon', form=form)
