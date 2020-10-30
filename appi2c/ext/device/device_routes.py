from flask import Blueprint, flash, redirect, render_template, url_for
from appi2c.ext.device.device_forms import DeviceSwitchForm, DeviceSensorForm
from appi2c.ext.group.group_controller import list_all_group
from appi2c.ext.mqtt.mqtt_controller import list_all_client_mqtt
from appi2c.ext.device.device_controller import (create_device_switch,
                                                 create_device_sensor,
                                                 list_all_device,
                                                 list_device_id,
                                                 get_inf_for_pub)
from flask_login import current_user


bp = Blueprint('devices', __name__, template_folder='appi2c/templates/device')


@bp.route("/select/type/device", methods=['GET', 'POST'])
def select_type_device():
    return render_template('device/device_type_select.html', title='Select Type Device')


def convert_qos(qos):
    if qos == '0':
        qos = 0
    elif qos == '1':
        qos = 1
    else:
        qos = 2
    return (qos)

@bp.route("/register/device/switch", methods=['GET', 'POST'])
def register_device_switch():
    group = list_all_group(current_user)
    if not group:
        flash(f'There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))
    client_mqtt = list_all_client_mqtt()
    if not client_mqtt:
        flash(f'There are no records. Register a Broker Mqtt', 'error')
        return redirect(url_for('mqtt.register'))
    form = DeviceSwitchForm()
    if form.validate_on_submit():

        qos_int = convert_qos(form.qos.data)

        create_device_switch(name=form.name.data,
                             topic_pub=form.topic_pub.data,
                             topic_sub=form.topic_sub.data,
                             command_on=form.command_on.data,
                             command_off=form.command_off.data,
                             last_will_topic=form.last_will_topic.data,
                             qos=qos_int,
                             retained=form.retained.data,
                             type_device='DeviceSwitch',
                             user=current_user.id,
                             group=form.groups.data.id)
        flash(f'Device '+ form.name.data +' has benn created!', 'success')
        return redirect(url_for('devices.list_device'))
    return render_template('device/device_create_switch.html', title='Register Device Switch', form=form)


@bp.route("/register/device/sensor", methods=['GET', 'POST'])
def register_device_sensor():
    group = list_all_group(current_user)
    if not group:
        flash(f'There are no records. Register a Group', 'error')
        return redirect(url_for('groups.register_group'))
    client_mqtt = list_all_client_mqtt()
    if not client_mqtt:
        flash(f'There are no records. Register a Broker Mqtt', 'error')
        return redirect(url_for('mqtt.register'))
    form = DeviceSensorForm()
    if form.validate_on_submit():

        qos_int = convert_qos(form.qos.data)

        create_device_sensor(group=form.groups.data.id,
                             name=form.name.data,
                             topic_pub=form.topic_pub.data,
                             topic_sub=form.topic_sub.data,
                             prefix=form.prefix.data,
                             postfix=form.postfix.data,
                             last_will_topic=form.last_will_topic.data,
                             qos=qos_int,
                             retained=form.retained.data,
                             type_device='DeviceSensor',
                             user=current_user.id,
                             )
        print(form.topic_sub.data)
        print(type(form.qos.data))

        #client_subscrib(form.topic_sub.data, int(form.qos.data))
        flash(f'Device ' + form.name.data + ' has benn created!', 'success')
        return redirect(url_for('devices.list_device'))
    return render_template('device/device_create_sensor.html', title='Register Device Sensor', form=form)


@bp.route("/list/device", methods=['GET', 'POST'])
def list_device():
    devices = list_all_device(current_user)
    if not devices:
        flash(f'There are no records. Register a Device', 'error')
        return redirect(url_for('devices.register_device_switch'))
    return render_template("device/device_list.html", title='Device List', devices=devices)


@bp.route("/teste", methods=['GET', 'POST'])
def teste():
    return render_template("device/device_teste.html")


@bp.route("/testeee<int:id>", methods=['GET', 'POST'])
def teste_device(id):
    if id == 1:
        '' #client_subscrib('teste/andre/sub', 1)
    else:
        '' #client_publish('teste/andre/pub', 'estou publicando', 1, False)
    return ''


@bp.route("/teste10", methods=['GET', 'POST'])
def teste10():
    return render_template("teste1.html")


@bp.route("/options/device", methods=['GET', 'POST'])
def device_opts():
    return render_template("device/device_opts.html", title='Device Options')


@bp.route("/admin/device", methods=['GET', 'POST'])
def admin_device():
    #groups = list_all_group(current_user)
    return 'admin/device'

@bp.route("/aboult/device")
def aboult_device():
    return render_template("device/device_aboult.html", title='Device Aboult')


@bp.route("/device/pub/<int:id>/<int:id_group>/<command>", methods=['GET', 'POST'])
def pub_device(id, id_group, command):
    device = list_device_id(id)
    get_inf_for_pub(device, command)
    print(command)
    return redirect(url_for('groups.content_group', id=id_group))