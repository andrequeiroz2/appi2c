from appi2c.ext.notifier.notifier_routes import bp
from appi2c.ext.admin import admin
from appi2c.ext.database import db
from appi2c.ext.notifier.notifier_models import Notifier
from appi2c.ext.notifier.notifier_admin import NotifierAdmin


def init_app(app):
    app.register_blueprint(bp)
    admin.add_view(NotifierAdmin(Notifier, db.session))
