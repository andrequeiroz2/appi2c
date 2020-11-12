from appi2c.ext.database import db
from appi2c.ext.group.group_models import Group 


def create_group(name: str, description: str, user: int):
    group = Group(name=name, description=description, user_id=user)
    db.session.add(group)
    db.session.commit()
    return group


def list_all_group(user):
    group = Group.query.filter_by(user_id=user.id).all()
    return group


def list_all_devices_in_group(group):
    devices_in_group = group.devices
    return devices_in_group


def delete_group_id(id):
    from appi2c.ext.device.device_controller import list_num_devices_in_group
    group = Group.query.filter_by(id=id).first() 
    list_device = list_num_devices_in_group(group)
    if list_device == 0:
        db.session.delete(group)
        db.session.commit()
        return True
    else:
        return False


def num_group():
    group = Group.query.all()
    num_group = len(group)
    return num_group


def num_group_user(user):
    group = Group.query.filter_by(id=user.id).all()
    num_group = len(group)
    return num_group


def list_group_id(id: int) -> Group:
    group = Group.query.filter_by(id=id).first()
    return group


def choice_query():
    return Group.query


def update_group(id: int, name: str, description: str):
    Group.query.filter_by(id=id).update(dict(name=name, description=description))
    db.session.commit()

