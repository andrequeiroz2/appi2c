from appi2c.ext.database import db


class TypeSwitch(db.Model):
    __tablename__ = "switch"
    id = db.Column('id', db.Integer, primary_key=True)
    on = db.Column('on', db.String(60), nullable=False)
    off = db.Column('off', db.String(60), nullable=False)


class TypeSensor(db.Model):
    __tablename__ = "sensor"
    id = db.Column('id', db.Integer, primary_key=True)
    prefix = db.Column('prefix', db.String(20), nullable=False)
    postfix = db.Column('postfix', db.String(20), nullable=False)


class TypeActuator(db.Model):
    __tablename__ = "actuator"
    id = db.Column('id', db.Integer, primary_key=True)
    prefix = db.Column('prefix', db.String(20), nullable=False)
    postfix = db.Column('postfix', db.String(20), nullable=False)
    command = db.Column('command', db.String(60), nullable=False)