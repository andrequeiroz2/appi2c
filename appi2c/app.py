from flask import Flask
from appi2c.ext import config
from appi2c.ext import socketio
from appi2c.ext.database import db
from appi2c.ext.database import db_commands
from appi2c.ext import mqtt
from appi2c.ext import device
from appi2c import migrate
from appi2c.ext.admin import admin
from appi2c.ext import auth
from appi2c.ext import login
from appi2c.ext import encrypt
from appi2c.ext import site
from appi2c.ext import group
from appi2c.ext import icon


def create_app():
    app = Flask(__name__)
    socketio.init_app(app)
    config.init_app(app)
    db.init_app(app)
    db.app = app
    #db.create_all()
    db_commands.init_app(app)
    mqtt.init_app(app)
    device.init_app(app)
    migrate.init_app(app)
    admin.init_app(app)
    auth.init_app(app)
    login.init_app(app)
    encrypt.init_app(app)
    site.init_app(app)
    group.init_app(app)
    icon.init_app(app)
    
    return app
