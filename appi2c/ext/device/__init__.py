from appi2c.ext.admin import admin
from appi2c.ext.database import db
from appi2c.ext.device.device_routes import bp
from appi2c.ext.device.device_admin import DeviceAdmin, DeviceTypeAdmin
from appi2c.ext.device.device_models import Device, DeviceType


def init_app(app):
    app.register_blueprint(bp)
    admin.add_view(DeviceAdmin(Device, db.session))
    admin.add_view(DeviceTypeAdmin(DeviceType, db.session))

    
