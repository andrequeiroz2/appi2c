from typing import NoReturn
from flask_login import login_required
from appi2c.ext.device.device_models import DeviceType
from flask import (Blueprint,
                   flash,
                   redirect,
                   render_template,
                   url_for,
                   request,
                   jsonify)
from appi2c.ext.device.device_forms import (DeviceSwitchForm,
                                            DeviceSensorForm,
                                            EditSwitchForm,
                                            EditSensorForm)
from appi2c.ext.group.group_controller import list_all_group
from appi2c.ext.mqtt.mqtt_controller import list_all_client_mqtt
from appi2c.ext.device.device_controller import (create_device_switch,
                                                 create_device_sensor,
                                                 list_all_device,
                                                 list_device_id,
                                                 get_inf_for_pub,
                                                 list_all_deviceType,
                                                 list_deviceType_id,
                                                 convert_qos,
                                                 convert_boolean,
                                                 update_device_switch,
                                                 delete_device_id,
                                                 get_position_icon)
from appi2c.ext.icon.icon_controller import list_all_icon
from flask_login import current_user


bp = Blueprint('devices', __name__, template_folder='appi2c/templates/device')


@bp.route("/register/device/switch", methods=['GET', 'POST'])
@login_required
def register_device_switch():
    group = list_all_group(current_user)
    icons = list_all_icon()
    if not group:
        flash('There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))
    client_mqtt = list_all_client_mqtt()
    if not client_mqtt:
        flash('There are no records. Register a Broker Mqtt', 'error')
        return redirect(url_for('mqtt.register_mqtt'))

    form = DeviceSwitchForm()
    if form.validate_on_submit():

        qos_int = convert_qos(form.qos.data)
        retain_bool = convert_boolean(form.retained.data)
        create_device_switch(name=form.name.data,
                             topic_pub=form.topic_pub.data,
                             topic_sub=form.topic_sub.data,
                             command_on=form.command_on.data,
                             command_off=form.command_off.data,
                             last_will_topic=form.last_will_topic.data,
                             qos=qos_int,
                             retained=retain_bool,
                             position_left='',
                             position_top='',
                             type_id=1,
                             icon_id=form.icon_id.data,
                             user=current_user.id,
                             group=form.groups.data.id)
        flash('Device ' + form.name.data + ' has benn created!', 'success')
        return redirect(url_for('devices.device_opts'))
    return render_template('device/device_create_switch.html',
                           title='Register Device Switch',
                           icons=icons,
                           form=form)


@bp.route("/register/device/sensor", methods=['GET', 'POST'])
@login_required
def register_device_sensor():
    group = list_all_group(current_user)
    icons = list_all_icon()
    if not group:
        flash('There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))
    client_mqtt = list_all_client_mqtt()
    if not client_mqtt:
        flash('There are no records. Register a Broker Mqtt', 'error')
        return redirect(url_for('mqtt.register_mqtt'))
    form = DeviceSensorForm()
    if form.validate_on_submit():
        qos_int = convert_qos(form.qos.data)
        retain_bool = convert_boolean(form.retained.data)
        create_device_sensor(name=form.name.data,
                             topic_pub=form.topic_pub.data,
                             topic_sub=form.topic_sub.data,
                             prefix=form.prefix.data,
                             postfix=form.postfix.data,
                             last_will_topic=form.last_will_topic.data,
                             qos=qos_int,
                             retained=retain_bool,
                             position_left='',
                             position_top='',
                             type_id=2,
                             icon_id=form.icon_id.data,
                             user=current_user.id,
                             group=form.groups.data.id,
                             )
        flash('Device ' + form.name.data + ' has benn created!', 'success')
        return redirect(url_for('devices.device_opts'))
    return render_template('device/device_create_sensor.html',
                           title='Register Device Sensor',
                           icons=icons,
                           form=form)


@bp.route("/list/device", methods=['GET', 'POST'])
@login_required
def list_device():
    devices = list_all_device(current_user)
    if not devices:
        flash('There are no records. Register a Device', 'error')
        return redirect(url_for('devices.device_opts'))
    return render_template("device/device_list.html",
                           title='Device List',
                           devices=devices)


@bp.route("/options/device", methods=['GET', 'POST'])
@login_required
def device_opts():
    types = list_all_deviceType()
    return render_template("device/device_opts.html",
                           title='Device Options',
                           types=types)


@bp.route("/admin/device", methods=['GET', 'POST'])
@login_required
def admin_device():
    devices = list_all_device(current_user)
    if not devices:
        flash('There are no records. Register a Device', 'error')
        return redirect(url_for('devices.device_opts'))
    return render_template('device/device_admin.html',
                           title='Device Admin',
                           devices=devices)


@bp.route("/pub", methods=['GET', 'POST'])
@login_required
def pub_device():
    action = request.form.get("command")
    print(action)
    s = action.split('/')
    command_device = s[1]
    id_device = int(s[0])
    device = list_device_id(id_device)
    get_inf_for_pub(device, command_device)

    device_id = str(device.id)
    device_last_date = device.last_date

    last_command = device.last_command
    if last_command == device.command_on:
        device_next_command = "Off"
        devive_commad = device.command_off
        device_color = "#ff6600"
    else:
        device_next_command = "On"
        devive_commad = device.command_on
        device_color = "#E9E2E0"
    return jsonify(id=device_id,
                   last_date=device_last_date,
                   next_command=device_next_command,
                   device_command=devive_commad,
                   device_color=device_color)


@bp.route("/get_position", methods=['POST'])
@login_required
def get_position():
    _json = request.json
    _id = int(_json["id"].split()[1])
    _left = _json["left"]
    _top = _json["top"]
    get_position_icon(_id, _left, _top)
    return jsonify({'message': 'position OK'})


@bp.route("/register/device/<int:id>", methods=['GET', 'POST'])
@login_required
def register_device(id):
    group = list_all_group(current_user)
    if not group:
        flash('There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))

    deviceType = list_deviceType_id(id)
    if deviceType.name == "Switch":
        return redirect(url_for('devices.register_device_switch'))
    else:
        deviceType.name == "Sensor"
        return redirect(url_for('devices.register_device_sensor'))


@bp.route('/edit/device/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_device(id):
    device_type = list_device_id(id)
    print("Device:", device_type.type_id)
    if device_type.type_id == 1:
        form = EditSwitchForm()
        current_device = list_device_id(id)

        if form.validate_on_submit():
            qos_int = convert_qos(form.qos.data)
            retain_bool = convert_boolean(form.retained.data)
            current_device.name = form.name.data
            current_device.topic_pub = form.topic_pub.data
            current_device.topic_sub = form.topic_sub.data
            current_device.command_on = form.command_on.data
            current_device.command_off = form.command_off.data
            current_device.last_will_topic = form.last_will_topic.data
            current_device.qos = qos_int
            current_device.retained = retain_bool
            current_device.groups = form.groups.data.id

            update_device_switch(id,
                                 current_device.name,
                                 current_device.topic_pub,
                                 current_device.topic_sub,
                                 current_device.command_on,
                                 current_device.command_off,
                                 current_device.last_will_topic,
                                 current_device.qos,
                                 current_device.retained,
                                 current_device.groups)

            flash('Your changes have been saved.', 'success')
            return redirect(url_for('devices.device_opts'))

        elif request.method == 'GET':
            form.name.data = current_device.name
            form.topic_pub.data = current_device.topic_pub
            form.topic_sub.data = current_device.topic_sub
            form.command_on.data = current_device.command_on
            form.command_off.data = current_device.command_off
            form.last_will_topic.data = current_device.last_will_topic
            form.qos.data = current_device.qos
            form.retained.data = current_device.retained
            form.groups.data = current_device.group_id

        return render_template('device/device_edit_switch.html',
                               title='Edit Device Switch',
                               form=form)

    if device_type.type_id == 2:
        form = EditSensorForm()
        current_device = list_device_id(id)

        if form.validate_on_submit():
            current_device.name = form.name.data
            current_device.topic_pub = form.topic_pub.data
            current_device.topic_sub = form.topic_sub.data
            current_device.prefix = form.prefix.data
            current_device.postfix = form.postfix.data
            current_device.last_will_topic = form.last_will_topic.data
            current_device.qos = form.qos.data
            current_device.retained = form.retained.data
            current_device.groups = form.groups.data

            update_device_switch(id,
                                 current_device.name,
                                 current_device.topic_pub,
                                 current_device.topic_sub,
                                 current_device.prefix,
                                 current_device.postfix,
                                 current_device.last_will_topic,
                                 current_device.qos,
                                 current_device.retained,
                                 current_device.groups)

            flash('Your changes have been saved.', 'success')
            return redirect(url_for('devices.device_opts'))

        elif request.method == 'GET':
            form.name.data = current_device.name
            form.topic_pub.data = current_device.topic_pub
            form.topic_sub.data = current_device.topic_sub
            form.prefix.data = current_device.prefix
            form.postfix.data = current_device.postfix
            form.last_will_topic.data = current_device.last_will_topic
            form.qos.data = current_device.qos
            form.retained.data = current_device.retained
            form.groups.data = current_device.groups

        return render_template('device/device_edit_sensor.html',
                               title='Edit Device Sensor',
                               form=form)
    return 'No type device'


@bp.route('/delete/device/<id>', methods=['GET', 'POST'])
@login_required
def delete_device(id):
    _id = int(id)
    delete_device_id(_id)
    flash('Device successfully deleted.', 'success')
    return redirect(url_for('devices.admin_device'))
