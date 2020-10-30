from flask_migrate import Migrate
from appi2c.ext.database import db

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)