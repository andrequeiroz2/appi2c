from appi2c.ext.database import db
from appi2c.ext.admin import admin
from appi2c.ext.auth.auth_admin import UserAdmin
from appi2c.ext.auth.auth_models import User
from appi2c.ext.auth.auth_routes import bp


def init_app(app):
    admin.add_view(UserAdmin(User, db.session))
    app.register_blueprint(bp)
