from appi2c.ext.database import db
from appi2c.ext.admin import admin
from appi2c.ext.group.group_admin import GroupAdmin
from appi2c.ext.group.group_routes import bp
from appi2c.ext.group.group_models import Group


def init_app(app):
    app.register_blueprint(bp)
    admin.add_view(GroupAdmin(Group, db.session))
