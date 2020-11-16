from flask import Blueprint
from flask import flash, redirect, url_for, render_template, request
from flask_login import current_user
from appi2c.ext.group.group_forms import GroupForm, EditGroupForm
from appi2c.ext.group.group_controller import (create_group,
                                               list_all_group,
                                               list_group_id,
                                               update_group,
                                               delete_group_id)

from appi2c.ext.device.device_controller import (list_num_devices_in_group,
                                                 list_device_in_group)

from appi2c.ext.icon.icon_controller import list_icon_in_device


bp = Blueprint('groups', __name__, template_folder="appi2c/templates/group")


@bp.route("/register/group", methods=['GET', 'POST'])
def register_group():
    form = GroupForm()
    if form.validate_on_submit():
        create_group(name=form.name.data.title(), description=form.description.data, user=current_user.id)
        flash('Group ' + form.name.data + ' has benn created!', 'success')
        return redirect(url_for('groups.list_group'))
    return render_template('group/group_create.html', title='Group Register', form=form)


@bp.route("/list/group", methods=['GET', 'POST'])
def list_group():
    groups = list_all_group(current_user)
    num_devices = list_num_devices_in_group(groups)
    if not groups:
        flash('There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))
    return render_template("group/group_list.html", title='Group List', obj=zip(groups, num_devices))


@bp.route("/aboult/group")
def aboult_group():
    return render_template("group/group_aboult.html", title='Group Aboult')


@bp.route("/admin/group", methods=['GET', 'POST'])
def admin_group():
    groups = list_all_group(current_user)
    if not groups:
        flash('There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))
    return render_template('group/group_admin.html', title='Group Admin', groups=groups)


@bp.route('/edit/group/<int:id>', methods=['GET', 'POST'])
def edit_group(id):
    form = EditGroupForm()
    current_group = list_group_id(id)
    if form.validate_on_submit():
        current_group.name = form.name.data
        current_group.description = form.description.data
        update_group(id, current_group.name, current_group.description)
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('groups.group_opts'))
    elif request.method == 'GET':
        form.name.data = current_group.name
        form.description.data = current_group.description
    return render_template('group/edit_group.html', title='Edit Group', form=form)


@bp.route('/delete/group/<int:id>', methods=['GET', 'POST'])
def delete_group(id):
    delete = delete_group_id(id)
    if delete:
        flash('Group successfully deleted.', 'success')
    else:
        flash('The group contains devices. First remove the devices.', 'error')
    return redirect(url_for('groups.admin_group'))


@bp.route("/options/group", methods=['GET', 'POST'])
def group_opts():
    return render_template("group/group_opts.html", title='Group Options')


@bp.route('/group/content/<int:id>', methods=['GET', 'POST'])
def content_group(id):
    group = list_group_id(id)
    devices = list_device_in_group(group)
    icons = list_icon_in_device(devices)
    return render_template('group/group_content.html', group=group, obj=zip(devices, icons))
