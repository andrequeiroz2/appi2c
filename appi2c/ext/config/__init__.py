import os
from appi2c.ext.database import db


def init_app(app):
    app.config["SECRET_KEY"] = "appi2c_from_raspberry"
    basedir = os.path.abspath(os.path.dirname('ext/database/'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
    app.config["MAX_IMAGE_FILESIZE"] = 10 * 1024 * 1024
    app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER_ENABLED"] = True
