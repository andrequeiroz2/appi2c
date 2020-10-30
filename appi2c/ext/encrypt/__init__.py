from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def init_app(app):
    bcrypt.init_app(app)