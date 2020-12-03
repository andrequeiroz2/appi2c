from flask_admin import Admin

admin = Admin()


def init_app(app):
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
