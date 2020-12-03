from werkzeug.wrappers import Response
from appi2c.ext.database import db
from appi2c.ext.group.group_models import Group
from flask import abort 
from flask.globals import current_app
from werkzeug.utils import secure_filename
from flask_login import current_user
import os
import imghdr
from flask import Response


def create_group(name: str, description: str, file: str, user: int):
    group = Group(name=name, description=description, file=file, user_id=user)
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


LOCAL_FOLDER = 'static/uploads/blueprints/'


def upload_files(uploaded_file):
    filename = secure_filename(uploaded_file.filename)
    if filename == '':
        return False
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1]
    if ext.upper() not in current_app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return False
    #if ext != validate_image(uploaded_file.stream):
    #    return False
    name_folder = current_user.username
    local_path = LOCAL_FOLDER + name_folder
    uploaded_file.save(os.path.join(local_path, filename))
    return True


def allowed_image_filesize(filesize):
    if int(filesize) <= current_app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


def folder_admin():
    name_folder = current_user.username
    local_path = LOCAL_FOLDER + name_folder
    if os.path.isdir(local_path):
        pass
    else:
        os.mkdir(local_path)


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


def get_image(id: int):
    group = Group.query.filter_by(id=id).first()
    username = str(current_user.username)
    image = str('/'+LOCAL_FOLDER+username+'/'+group.file)
    return image
