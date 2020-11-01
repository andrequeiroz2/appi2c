from appi2c.ext.group.group_models import Group
from appi2c.ext.database import db
from appi2c.ext.device.device_models import Device, DeviceType
from datetime import datetime
from appi2c.ext.mqtt.mqtt_connect import handle_publish


def get_date():
    date_now = datetime.now()
    date_time_now = date_now.strftime('%d/%m/%Y %H:%M')
    return date_time_now


def create_device_switch(name: str,
                         topic_pub: str,
                         topic_sub: str,
                         command_on: str,
                         command_off: str,
                         last_will_topic: str,
                         qos: int,
                         retained: bool,
                         type_device: str,
                         user: int,
                         group: int):

    device = Device(name=name,
                    topic_pub=topic_pub,
                    topic_sub=topic_sub,
                    command_on=command_on,
                    command_off=command_off,
                    last_command=command_off,
                    last_date='',
                    last_will_topic=last_will_topic,
                    qos=qos,
                    retained=retained,
                    type_device=type_device,
                    user_id=user,
                    group_id=group)
    db.session.add(device)
    db.session.commit()
    return device


def create_device_sensor(group: int,
                         name: str,
                         topic_pub: str,
                         topic_sub: str,
                         prefix: str,
                         postfix: str,
                         last_will_topic: str,
                         qos: int,
                         retained: bool,
                         type_device: str,
                         user: int,
                         ):

    device = Device(group_id=group,
                    name=name,
                    topic_pub=topic_pub,
                    topic_sub=topic_sub,
                    prefix=prefix,
                    postfix=postfix,
                    last_will_topic=last_will_topic,
                    qos=qos,
                    retained=retained,
                    type_device=type_device,
                    user_id=user,
                    )
    db.session.add(device)
    db.session.commit()
    return device


def list_all_device(user):
    device = user.devices
    return device


def num_device():
    device = Device.query.all()
    num_device = len(device)
    return num_device


def num_device_in_user(user):
    device = Device.query.filter_by(user_id=user.id).all()
    num_device = len(device)
    return num_device


def list_num_devices_in_group(group):
    if isinstance(group, list):
        len_group = (len(group))
        num_device = []
        for x in range(len_group):
            group_id = group[x]
            device_id = Device.query.filter_by(group_id=group_id.id).all()
            num_device.append(len(device_id))
        return num_device
    else:
        device_id = Device.query.filter_by(group_id=group.id).all()
        num_device = (len(device_id))
        return num_device


def list_device_in_group(group):
    device = Device.query.filter_by(group_id=group.id).all()
    return device


def list_device_id(id: int):
    device = Device.query.filter_by(id=id).first()
    return device


def list_all_deviceType():
    deviceType = DeviceType.query.all()
    return deviceType


def list_deviceType_id(id: int):
    deviceType = DeviceType.query.filter_by(id=id).first()
    return deviceType


def get_inf_for_pub(device, command):
    topic = device.topic_pub
    qos = device.qos
    retain = device.retained
    if command == 'command_off':
        msg = device.command_off
        device.last_command = device.command_off
    else:
        msg = device.command_on
        device.last_command = device.command_on
    handle_publish(topic, msg, qos, retain)
    date_now = get_date()
    device.last_date = date_now
    db.session.commit()

