from appi2c.ext.admin import admin
from appi2c.ext.database import db
from appi2c.ext.icon.icon_routes import bp
from appi2c.ext.icon.icon_admin import IconAdmin
from appi2c.ext.icon.icon_models import Icon


def init_app(app):
    app.register_blueprint(bp)
    admin.add_view(IconAdmin(Icon, db.session))
