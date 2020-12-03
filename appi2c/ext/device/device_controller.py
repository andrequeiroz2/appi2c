from appi2c.ext.group.group_models import Group
from appi2c.ext.database import db
from appi2c.ext.device.device_models import Device, DeviceType
from datetime import datetime
from appi2c.ext.mqtt.mqtt_connect import (handle_publish,
                                          handle_subscribe)


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
                         position_left: str,
                         position_top: str,
                         type_id: int,
                         icon_id: int,
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
                    position_left=position_left,
                    position_top=position_top,
                    icon_id=icon_id,
                    type_id=type_id,
                    user_id=user,
                    group_id=group)
    db.session.add(device)
    db.session.commit()


def create_device_sensor(group: int,
                         name: str,
                         topic_pub: str,
                         topic_sub: str,
                         prefix: str,
                         postfix: str,
                         last_will_topic: str,
                         qos: int,
                         retained: bool,
                         position_left: str,
                         position_top: str,
                         icon_id: int,
                         type_id: int,
                         user: int,):

    device = Device(group_id=group,
                    name=name,
                    topic_pub=topic_pub,
                    topic_sub=topic_sub,
                    prefix=prefix,
                    postfix=postfix,
                    last_will_topic=last_will_topic,
                    qos=qos,
                    retained=retained,
                    position_left=position_left,
                    position_top=position_top,
                    icon_id=icon_id,
                    type_id=type_id,
                    user_id=user)
    db.session.add(device)
    db.session.commit()
    handle_subscribe(topic_sub, qos)


def convert_boolean(result: str):
    if result == 'True':
        value = True
        return value
    else:
        value = False
        return value


def convert_qos(qos: str) -> int:
    if qos == '0':
        value = 0
    elif qos == '1':
        value = 1
    else:
        value = 2
    return value


def list_all_device_init():
    device = Device.query.all()
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
    if command == device.command_off:
        msg = device.command_off
        device.last_command = device.command_off
    else:
        msg = device.command_on
        device.last_command = device.command_on
    handle_publish(topic, msg, qos, retain)
    date_now = get_date()
    device.last_date = date_now
    db.session.commit()


def get_inf_all_device_sub():
    devices = list_all_device_init()
    if not devices:
        pass
    else:
        for device in devices:
            if not device.topic_sub:
                pass
            else:
                topic = device.topic_sub
                qos = device.qos
                print(qos)
                handle_subscribe(topic, qos)


def update_device_switch(id: int,
                         name: str,
                         topic_pub: str,
                         topic_sub: str,
                         prefix: str,
                         postfix: str,
                         last_will_topic: str,
                         qos: int,
                         retained: bool,
                         group_id: int):

    Device.query.filter_by(id=id).update(dict(name=name, 
                                              topic_pub=topic_pub,
                                              topic_sub=topic_sub,
                                              prefix=prefix,
                                              postfix=postfix,
                                              last_will_topic=last_will_topic,
                                              qos=qos,
                                              retained=retained,
                                              group_id=group_id))
    db.session.commit()


def delete_device_id(id):
    device = Device.query.filter_by(id=id).first()
    db.session.delete(device)
    db.session.commit()


def get_position_icon(id: int, left: str, top: str):
    device = Device.query.filter_by(id=id).first()
    if device.position_left == left:
        pass
    else:
        device.position_left = left
    if device.position_top == top:
        pass
    else:
        device.position_top = top
    db.session.commit()
