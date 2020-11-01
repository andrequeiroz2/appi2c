from appi2c.ext.database import db


class Device(db.Model):
    __tablename__ = "device"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(60), nullable=False)
    topic_pub = db.Column('topic_pub', db.String(120))
    topic_sub = db.Column('topic_sub', db.String(120))
    last_will_topic = db.Column('last_will_topic', db.String(60))
    command_on = db.Column('command_on', db.String(60))
    command_off = db.Column('command_off', db.String(60))
    last_command = db.Column('last_command', db.String(60))
    last_date = db.Column('last_date', db.String(60))
    prefix = db.Column('prefix', db.String(10))
    postfix = db.Column('postfix', db.String(10))
    qos = db.Column('qos', db.Integer, nullable=False)
    retained = db.Column("retained", db.String(5), default='True')
    type_id = db.Column('type_id', db.Integer, db.ForeignKey('device_type.id'), nullable=False)
    icon_id = db.Column('icon_id', db.Integer, db.ForeignKey('icon.id'), nullable=False)
    group_id = db.Column('group_id', db.Integer, db.ForeignKey('group.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Device('{self.name}',\
                        '{self.topic_pub}',\
                        '{self.topic_pub}',\
                        '{self.last_will_topic}',\
                        '{self.qos}',\
                        '{self.retained}')"


class DeviceType(db.Model):
    __tablename__ = "device_type"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(60))
    devices = db.relationship('Device', backref='device', lazy=True)


    def __repr__(self):
        return f"'{self.name}'"

    def validate_name(self, key, name):
        if not name:
            raise AssertionError('No name provided')
        if DeviceType.query.filter(DeviceType.name == name).first():
            raise AssertionError('Name is already in use')
