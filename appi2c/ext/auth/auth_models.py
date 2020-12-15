import re
from appi2c.ext.database import db
from sqlalchemy.orm import validates
from flask_login import UserMixin
from appi2c.ext.login import login


@login.user_loader
def load_ser(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(30), index=True, nullable=False)
    email = db.Column("email", db.String(120), index=True, nullable=False)
    password = db.Column(db.String(128))
    admin = db.Column("admin", db.Boolean, default=False)
    groups = db.relationship('Group', backref='user', lazy=True)
    devices = db.relationship('Device', backref='user', lazy=True)
    client_mqtt = db.relationship('ClientMqtt', backref='user', lazy='dynamic')

    def __repr__(self):
        return f"('{self.id}',{self.username},'{self.email}','{self.admin}')"

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')

        #if User.query.filter(User.username == username).first():
        #    raise AssertionError('Username is already in use')

        if len(username) < 5 or len(username) > 30:
            raise AssertionError('Username must be between 5 and 30 characters')
        return username

    @validates('email')
    def validade_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')
        return email

    @validates('password')
    def validade_passwd(self, key, password):
        if not password:
            raise AssertionError('No password provided')
        return password
