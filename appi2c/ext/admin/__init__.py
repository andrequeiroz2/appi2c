from flask_admin import Admin
from appi2c.ext.database import db


admin = Admin()


def init_app(app):
    admin.name = 'Admin'
    admin.base_template = 'my_master.html'
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
