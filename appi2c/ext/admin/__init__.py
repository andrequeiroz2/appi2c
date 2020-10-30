from flask_admin import Admin

admin = Admin()


def init_app(app):
    admin.name="appi2c"
    admin.template_mode="bootstrap2"
    admin.init_app(app)