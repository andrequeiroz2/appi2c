from appi2c.ext.database import db
from appi2c.ext.group.group_models import Group
from appi2c.ext.device.device_models import Device, Data, DeviceType, Limit
import datetime
from appi2c.ext.mqtt.mqtt_connect import (handle_publish,
                                          handle_subscribe)
from appi2c.ext.notifier.notifier_controller import notifier_sendtext, list_notifier_id


def get_date():
    date_now = datetime.datetime.now()
    return date_now


def create_device_switch(name: str,
                         topic_pub: str,
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
    if last_will_topic is not None:
        handle_subscribe(last_will_topic, qos)


def create_device_sensor(group: int,
                         name: str,
                         topic_sub: str,
                         measure: str,
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
                    measure=measure,
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
                         command_on: str,
                         command_off: str,
                         last_will_topic: str,
                         qos: int,
                         retained: bool,
                         group_id: int,
                         icon_id: int):

    Device.query.filter_by(id=id).update(dict(name=name,
                                              topic_pub=topic_pub,
                                              command_on=command_on,
                                              command_off=command_off,
                                              last_will_topic=last_will_topic,
                                              qos=qos,
                                              retained=retained,
                                              group_id=group_id,
                                              icon_id=icon_id))
    db.session.commit()


def update_device_sensor(id: int,
                         name: str,
                         topic_sub: str,
                         measure: str,
                         postfix: str,
                         last_will_topic: str,
                         qos: int,
                         group_id: int,
                         icon_id: int):

    Device.query.filter_by(id=id).update(dict(name=name,
                                              topic_sub=topic_sub,
                                              measure=measure,
                                              postfix=postfix,
                                              last_will_topic=last_will_topic,
                                              qos=qos,
                                              group_id=group_id,
                                              icon_id=icon_id))
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
                x.last_data = payload
                db.session.commit()
            db.engine.execute(Data.__table__.insert(), device_list)


def check_difference_date(limit):
    date_bd = limit.date_time
    if date_bd is None:
        return True
    else:
        date_now = get_date()
        x = date_now - date_bd
        minutes = int(x.seconds / 60)
        if minutes >= 5:
            return True
        else:
            return False


def check_data_limit(topic, payload):
    if not payload or not payload.strip():
        pass
    else:
        device = Device.query.filter_by(topic_sub=topic).all()
        if device:
            for x in device:
                device_limit = Limit.query.filter_by(device_id=x.id).first()
                if device_limit:
                    difference_date = check_difference_date(device_limit)
                    if difference_date:
                        device_type = DeviceType.query.filter_by(id=x.type_id).first()
                        notifier = list_notifier_id(device_limit.notifier_id)
                        if device_type.name == 'Sensor':
                            payload_int = int(payload)
                            if device_limit.limit_max != '' and device_limit.limit_max < payload_int:
                                register_limits_date(device_limit)
                                message = create_sendtext(x, payload)
                                notifier_sendtext(notifier, message)
                            elif device_limit.limit_min != '' and device_limit.limit_min > payload_int:
                                register_limits_date(device_limit)
                                message = create_sendtext(x, payload)
                                notifier_sendtext(notifier, message)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        else:
            pass


def create_sendtext(device: Device, payload):
    group = Group.query.filter_by(id=device.group_id).first()
    limit = Limit.query.filter_by(device_id=device.id).first()
    type = DeviceType.query.filter_by(id=device.type_id).first()

    title = 'This is an automatic message from appi2c.\n'
    attention = 'Attention device with readings outside the appropriate limits.\n'
    space = '\n'
    level = 'Warning level: ' + limit.level + '\n'
    device_details = 'Device Name: ' + device.name + '\n'\
                     'Device Type: ' + type.name + '\n'\
                     'Device Meassure: ' + device.measure + '\n'\
                     'Device Group: ' + group.name + '\n'

    limit_details = 'Maximum limit: ' + str(limit.limit_max) + device.postfix + '\n'\
                    'Minimum limit: ' + str(limit.limit_min) + device.postfix + '\n'

    last_data = 'Device Last Reading: ' + payload + device.postfix + '\n'

    date = 'DateTime: ' + str(limit.date_time.strftime("%Y"+"/"+"%m"+"/"+"%d"+" "+"%H"+":"+"%M"))+ '\n'

    end = 'If the values ​​remain outside the limits, you will be notified again in 5 minutes.'

    message = title+attention+space+level+space+device_details+limit_details+space+last_data+space+date+space+end

    return message


def get_data_id(id: int, payload: str):
    if not payload or not payload.strip():
        pass
    else:
        device = Device.query.filter_by(id=id).first()
        if device:
            device_data_dict = {'data': payload,
                                'date_time': get_date(),
                                'device_id': device.id}
            db.engine.execute(Data.__table__.insert(), device_data_dict)


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
    delete_limit_id(id)
    device = Device.query.filter_by(id=id).first()
    db.session.delete(device)
    db.session.commit()


def delete_data_id(id: int):
    delete = Data.__table__.delete().where(Data.device_id == id)
    db.session.execute(delete)
    db.session.commit()


def delete_limit_id(id: int):
    delete = Limit.__table__.delete().where(Limit.device_id == id)
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


def check_register_device(id: int) -> bool: 
    check = Limit.query.filter_by(device_id=id).first()
    if check:
        return True
    else:
        return False


def register_limits_device(limit_max: int,
                           limit_min: int,
                           level: str,
                           device_id: int,
                           notifier_id: int):

    limit = Limit(limit_max=limit_max,
                  limit_min=limit_min,
                  level=level,
                  device_id=device_id,
                  notifier_id=notifier_id)

    db.session.add(limit)
    db.session.commit()


def register_limits_date(limits):
    limits.date_time = get_date()
    db.session.commit()


def update_limits_device(limit_max: int,
                         limit_min: int,
                         level: str,
                         device_id: int,
                         notifier_id: int):

    Limit.query.filter_by(device_id=device_id).update(dict(limit_max=limit_max,
                                                           limit_min=limit_min,
                                                           level=level,
                                                           device_id=device_id,
                                                           notifier_id=notifier_id))
    db.session.commit()


def list_limit_device_id(id: int) -> Limit:
    limits = Limit.query.filter_by(device_id=id).first()
    return limits


def list_limit_notifier_id(id: int) -> Limit:
    limits = Limit.query.filter_by(notifier_id=id).first()
    return limits
