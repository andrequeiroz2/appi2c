from appi2c.ext.database import db
from appi2c.ext.icon.icon_models import Icon


def list_all_icon():
    icon = Icon.query.all()
    return icon


def list_icon_id(id: int) -> Icon:
    icon = Icon.query.filter_by(id=id).first()
    return icon


def create_icon(html_class: str):
    icon = Icon(html_class=html_class)
    db.session.add(icon)
    db.session.commit()


def update_icon(id: int, html_class: str):
    Icon.query.filter_by(id=id).update(dict(html_class=html_class))
    db.session.commit()


def list_icon_in_device(devices: list):
    if devices is not None:
        list_icon = []
        for device in devices:
            icon = Icon.query.filter_by(id=device.icon_id).first()
            list_icon.append(icon.html_class)
        return list_icon
    return False
