from appi2c.ext.database import db
from appi2c.ext.icon.icon_models import Icon


def list_all_icon():
    icon = Icon.query.all()
    return icon
