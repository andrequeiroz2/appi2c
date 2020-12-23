from appi2c.ext.database import db
from appi2c.ext.group.group_models import Group
from appi2c.ext.device.device_models import Device, Data, DeviceType
import datetime
from appi2c.ext.mqtt.mqtt_connect import (handle_publish,
                                          handle_subscribe)


def get_date():
    date_now = datetime.datetime.now()
    return date_now


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
                    last_date=get_date(),
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
    #handle_subscribe(topic_pub, qos)
    if last_will_topic is not None:
        handle_subscribe(last_will_topic, qos)


def create_device_sensor(group: int,
                         name: str,
                         topic_sub: str,
                         prefix: str,
                         postfix: str,
                         last_will_topic: str,
                         qos: int,
                         position_left: str,
                         position_top: str,
                         icon_id: int,
                         type_id: int,
                         user: int):

    device = Device(group_id=group,
                    name=name,
                    topic_sub=topic_sub,
                    last_date=get_date(),
                    last_data='',
                    prefix=prefix,
                    postfix=postfix,
                    last_will_topic=last_will_topic,
                    qos=qos,
                    position_left=position_left,
                    position_top=position_top,
                    icon_id=icon_id,
                    type_id=type_id,
                    user_id=user)
    db.session.add(device)
    db.session.commit()

    handle_subscribe(topic_sub, qos)
    if last_will_topic:
        handle_subscribe(last_will_topic, qos)
    else:
        pass


def update_device_switch(id: int,
                         name: str,
                         topic_pub: str,
                         topic_sub: str,
                         command_on: str,
                         command_off: str,
                         last_will_topic: str,
                         qos: int,
                         retained: bool,
                         group_id: int):

    Device.query.filter_by(id=id).update(dict(name=name,
                                              topic_pub=topic_pub,
                                              topic_sub=topic_sub,
                                              command_on=command_on,
                                              command_off=command_off,
                                              last_will_topic=last_will_topic,
                                              qos=qos,
                                              retained=retained,
                                              group_id=group_id))
    db.session.commit()


def update_device_sensor(id: int,
                         name: str,
                         topic_sub: str,
                         prefix: str,
                         postfix: str,
                         last_will_topic: str,
                         qos: int,
                         group_id: int):

    Device.query.filter_by(id=id).update(dict(name=name,
                                              topic_sub=topic_sub,
                                              prefix=prefix,
                                              postfix=postfix,
                                              last_will_topic=last_will_topic,
                                              qos=qos,
                                              group_id=group_id))
    db.session.commit()
    handle_subscribe(topic_sub, qos)
    if last_will_topic:
        handle_subscribe(last_will_topic, qos)
    else:
        pass


def get_data(topic, payload):
    if not payload or not payload.strip():
        pass
    else:
        device = Device.query.filter_by(topic_sub=topic).all()
        device_list = []
        if device:
            for x in device:
                device_data_dict = {'data': payload,
                                    'date_time': get_date(),
                                    'device_id': x.id}
                device_list.append(device_data_dict)
            db.engine.execute(Data.__table__.insert(), device_list)

        #device_pub = Device.query.filter_by(topic_pub=topic).all()
        #if device_pub:
        #    insert_inf_in_devices(device_pub, payload)


#def insert_inf_in_devices(device: list, payload: str):
    #if device:
    #    for x in device:
    #        device_obj = list_device_id(x.id)
    #        if device_obj.type_id == 1:
    #            if (device_obj.command_on == payload) or (device_obj.command_off == payload):
    #                device_obj.last_command = payload
    #                device_obj.last_date = get_date()
    #        if device_obj.type_id == 2:
    #            device_obj.last_data = payload
    #            device_obj.last_date = get_date()
    #        db.session.commit()
#    return ''

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
    topic_pub = device.topic_pub
    qos = device.qos
    retain = device.retained

    if command == device.command_off:
        print('Command', command)
        msg = device.command_off
        device.last_command = device.command_off
    else:
        print('Command', command)
        msg = device.command_on
        device.last_command = device.command_on

    date_now = get_date()
    device.last_date = date_now
    db.session.commit()
    handle_publish(topic_pub, msg, qos, retain)


def get_inf_all_device_sub():
    devices = list_all_device_init()
    if devices:
        for device in devices:
            if device.type_id == 1:
                topic = device.topic_pub
                qos = device.qos
                handle_subscribe(topic, qos)

            if device.type_id == 2:
                topic = device.topic_sub
                qos = device.qos
                handle_subscribe(topic, qos)


def delete_device_id(id: int):
    delete_data_id(id)
    device = Device.query.filter_by(id=id).first()
    db.session.delete(device)
    db.session.commit()


def delete_data_id(id: int):
    delete = Data.__table__.delete().where(Data.device_id == id)
    db.session.execute(delete)
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


def get_clear_topic(topic: str):
    handle_publish(topic, '', qos=2, retain=True)
    return True


def get_data_historic(id: int):
    data = Data.query.filter_by(device_id=id).all()
    return data


def get_datetime(data: list):
    data_dict = {"data": [], "date": []}
    for x in data:
        date = x.date_time.strftime("%Y"+"/"+"%m"+"/"+"%d"+" "+"%H"+":"+"%M")
        print(date)
        data_dict["data"].append(x.data)
        data_dict["date"].append(date)
    return data_dict
