from appi2c.ext.database import db
from appi2c.ext.icon.icon_models import Icon


def list_all_icon():
    icon = Icon.query.all()
    return icon


def list_icon_id(id: int) -> Icon:
    icon = Icon.query.fliter_by(id=id).first()
    return icon


def create_icon(html_class: str):
    icon = Icon(html_class=html_class)
    db.session.add(icon)
    db.session.commit()


def update_icon(id: int, html_class: str):
    Icon.query.filter_by(id=id).update(dict(html_class=html_class))
    db.session.commit()
